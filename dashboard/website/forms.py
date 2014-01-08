# coding: utf-8

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import validate_email

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

    def validate(self, forgot_password_token, *args, **kw):
        if self.is_valid():
            password = self.data.get('password')
            password_conf = self.data.get('password_conf')
        
            if password != password_conf:
                self.errors.update({'invalid': 'Passwords miss match.'})
                return False
            return True
        else:
            self.errors.update({'invalid': 'You can not leave a blank field.'})
            return False
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="e-mail:")

    def validate(self, *args, **kw):
        if self.is_valid():
            email = self.data.get('email')
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user:
                if user.is_active:
                    try:
                        dashboarduser = DashboardUser.objects.get(user=user)
                        return True
                    except:
                        self.errors.update({'invalid': 'You can\'t change this user password.'})
                        return False
                else:
                    self.errors.update({'invalid': 'User is inactive.'})
            else:
                self.errors.update({'invalid': 'Email does not exist on our database.'})
        else:
            self.errors.update({'invalid': 'Email is invalid.'})
        
        return False

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password', 'size':20, 'maxlength':20}), max_length=100, label=u"old password:")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password', 'size':20, 'maxlength':20}), max_length=100, label=u"new password:")
    new_password_conf = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password Confirmation', 'size':20, 'maxlength':20}), max_length=100, label=u"new password confirmation:")

    def validate(self, user, *args, **kw):
        if self.is_valid():
            old_password = self.data.get('old_password')
            new_password = self.data.get('new_password')
            new_password_conf = self.data.get('new_password_conf')
            
            if user.check_password(old_password):
                if new_password == new_password_conf:
                    return True
                else:
                    self.errors.update({'invalid': 'Passwords miss match.'})
            else:
                self.errors.update({'invalid': 'Wrong password.'})
        else:
            self.errors.update({'invalid': 'You can not leave a blank field.'})
        
        return False
