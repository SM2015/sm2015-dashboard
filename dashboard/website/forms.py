# coding: utf-8

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from core.models import DashboardUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'e-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), max_length=100)

    def validate(self, *args, **kw):
        if self.is_valid():
            user = self.get_user()
            if user:
                return True
            else:
                self.errors.update({'invalid': 'Username or Password is incorrect'})
        else:
            self.errors.update({'invalid': 'Please, fulfill fields correctly'})
        
        return False

    def get_user(self):
        username = self.data.get('username')
        password = self.data.get('password')

        try:
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

class SetPasswordForm(forms.Form):
    password         = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'size':20, 'maxlength':20}), max_length=100, label=u"password:")
    password_conf    = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password confirmation', 'size':20, 'maxlength':20}), max_length=100, label=u"password confirmation:")
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="e-mail:")
