from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import *
from .forms import Account_form


class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'user_type')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    """
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),                               #css
            'fields': ('email', 'password1', 'password2')}      #user creation fields
         ),
    )

    #form = UserChangeForm
    add_form = Account_form
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_superuser') #lenteles stulpeliai
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_admin', 'user_type') #sone esantis filtras
    search_fields = ('first_name', 'last_name', 'email')  #virsuje atsiranda paieskos laukelis
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)


admin.site.register(Account, UserAdmin)


#Account modelyje reikia prideti permissionMixin kad veiktu