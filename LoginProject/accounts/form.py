import re
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']

        if not re.fullmatch(r'[A-Za-z0-9_]{5,15}', username):
            raise forms.ValidationError("Invalid Username")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if not re.fullmatch(r'(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@_!]{8,}', password):
            raise forms.ValidationError(
                "Password must contain at least 8 characters, a letter and a number"
            )

        return password