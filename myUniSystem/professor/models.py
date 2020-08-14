from django.db import models
from account.models import Account
from subjects.models import Subject


class Professor(models.Model):

    phone = models.CharField(max_length=100)
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    code = models.CharField(max_length=20)
    subjects = models.ManyToManyField(Subject, related_name='professors')

    def __str__(self):
        return  self.code + " " + self.account.first_name + " " + self.account.last_name

