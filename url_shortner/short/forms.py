from django import forms
from .models import UserProfileInfo,Bitly
from django.contrib.auth.models import User
from . import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','password']


class UserProfileInfoForm(forms.ModelForm):
    con_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ['full_name','mobile']

class Sign_in(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['email','password']

class CreateSortCode(forms.ModelForm):
    class Meta:
        model = models.Bitly
        fields = ['long_url']