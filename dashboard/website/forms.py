# coding: utf-8

from django import forms
from django.conf import settings
from django.contrib.auth.models import User

from core.models import DashboardUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'e-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), max_length=100)
 
class RegisterForm(forms.Form):

    first_name  = forms.CharField(label="first name", widget=forms.TextInput(attrs={'placeholder': 'first name', 'size':30, 'maxlength':30}))
    last_name   = forms.CharField(label="last name", widget=forms.TextInput(attrs={'placeholder': 'last name', 'size':30, 'maxlength':30}))
    email       = forms.EmailField(label="e-mail", widget=forms.TextInput(attrs={'placeholder': 'e-mail', 'size':50, 'maxlength':50}))

    def clean_email(self):
        try:
            email = self.cleaned_data.get('email')
            if email and User.objects.filter(email=email).count() > 0:
                raise forms.ValidationError(u'Esse e-mail já foi utilizado.')
        except User.DoesNotExist:
            pass

        return email

    def clean_first_name(self):
        if len(self.data.get('first_name', '').strip()) < 3:
            raise forms.ValidationError("required field and it needs 3 or more characters.")
            
        return self.data.get('first_name')

    def clean_last_name(self):
        if len(self.data.get('last_name', '').strip()) < 3:
            raise forms.ValidationError("required field and it needs 3 or more characters.")
            
        return self.data.get('last_name')

    def save(self, *args, **kwargs):
        
        
        email = self.cleaned_data.get('email')
        username =  email
        
        new_user = User.objects.create_user( 
                                    username,
                                    self.cleaned_data.get('email'),
                                )
        
        new_user.is_active = False
        new_user.first_name = self.cleaned_data.get('first_name')
        new_user.last_name = self.cleaned_data.get('last_name')
        
        new_user.save()
        
        new_profile = DashboardUser()
        new_profile.user = new_user
        new_profile.save()
        
        return new_profile

class SetPasswordForm(forms.Form):
    password         = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'size':20, 'maxlength':20}), max_length=100, label=u"password:")
    password_conf    = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password confirmation', 'size':20, 'maxlength':20}), max_length=100, label=u"password confirmation:")
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="e-mail:")