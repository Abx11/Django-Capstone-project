# user_auth/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
