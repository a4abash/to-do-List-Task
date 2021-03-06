from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


# User creation form
class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'username'}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}), required=True, label="Password")

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Re-type your password'}), required=True, label="Password Confirmation")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']