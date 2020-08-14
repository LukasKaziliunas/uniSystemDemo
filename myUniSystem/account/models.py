from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import models as auth_models

class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Email required")
        if not first_name:
            raise ValueError("Name required")
        if not last_name:
            raise ValueError("Last name required")

        user = self.model(
            email       = self.normalize_email(email),
            first_name  = first_name,
            last_name   = last_name,
        )

        user.username = first_name[:3].lower() + last_name[:3].lower()

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            first_name= "admin",
            last_name= "admin",
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, auth_models.PermissionsMixin):

    STUDENT     = 1
    PROFESSOR   = 2
    STAFF       = 3
    UNDEFINED   = 4

    TYPE = (
        (STUDENT, 'student'),
        (PROFESSOR, 'professor'),
        (STAFF, 'staff'),
        (UNDEFINED, 'undefined'),
    )

    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username        = models.CharField(max_length=60, unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    first_name      = models.CharField(max_length=250)
    last_name       = models.CharField(max_length=250)
    user_type       = models.IntegerField(choices=TYPE, default=4)

    USERNAME_FIELD = 'email'

    objects = MyAccountManager()

    def __str__(self):
        if self.user_type == self.STUDENT:
            return self.first_name + " " + self.last_name + " -stud"
        elif self.user_type == self.PROFESSOR:
            return self.first_name + " " + self.last_name + " -prof"
        else:
            return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

