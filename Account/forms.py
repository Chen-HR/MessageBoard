from django import forms
from Account.models import User

class SignupForm(forms.Form):
  Account    = forms.CharField(max_length=32, initial='')
  Password   = forms.CharField(max_length=32, initial='')
  RePassword = forms.CharField(max_length=32, initial='')
  Name       = forms.CharField(max_length=64, initial='')
  Phone      = forms.CharField(max_length=64, initial='', required=False)
  Email      = forms.EmailField(max_length=256, initial='', required=False)

class LoginForm(forms.Form):
  Account    = forms.CharField(max_length=32, initial='')
  Password   = forms.CharField(max_length=32, initial='')

