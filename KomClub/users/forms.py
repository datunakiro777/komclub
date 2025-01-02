from django import forms
from .models import User_info

class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    class Meta:
        model = User_info
        fields = ['username','last_name', 'gmail', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Username")
    last_name = forms.CharField(max_length=20, label='Last Name')
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
