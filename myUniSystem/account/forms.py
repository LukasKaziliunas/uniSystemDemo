from django import forms
from django.contrib.auth.forms import UserCreationForm
from student.models import Student

from django.contrib.auth import authenticate
from account.models import Account

class Account_form(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "password1", "password2")

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('code', 'avarageScore', 'account', 'subjects')

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
            model = Account
            fields = ('email', 'password')

    def clean(self):
         email = self.cleaned_data['email']
         password = self.cleaned_data['password']
         if not authenticate(email=email, password=password):
              raise forms.ValidationError("invalid login")