# coding: utf-8

import random
import sha
import logging
import json

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.forms.util import ErrorList
from django.forms.forms import NON_FIELD_ERRORS

from website.forms import LoginForm, SetPasswordForm, ForgotPasswordForm, ChangePasswordForm
from core.models import *
from map.models import Map

@login_required
def index(request):
    maps = Map.objects.all()
    countries_map = []
    for country_map in maps:
        country = {
            'lat': str(country_map.country.latlng.split(',')[0]),
            'lng': str(country_map.country.latlng.split(',')[1]),
            'name': str(country_map.country.name),
            'goal': str(country_map.goal),
            'short_description': str(country_map.short_description)
        }
        countries_map.append(country)

    context = RequestContext(request)
    context.update({'user_name': context.get('user').first_name})
    context.update({'countries_map': countries_map})

    return render_to_response('index.html', context)

def dashboard_login(request):
    context = RequestContext(request)
    if context.get('user').is_authenticated():
        return redirect('index')

    if request.method == "POST":
        form_login = LoginForm(request.POST)
        if form_login.validate():
            user = form_login.get_user()
            login(request, user)
            if request.POST.get('remember', None):
                request.session.set_expiry(0)
            return redirect('index')
    else:
        form_login = LoginForm()
    context.update({'form_login': form_login})
    return render_to_response('login.html',
                          context_instance=context)

def dashboard_logout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect("dashboard_login")

def forgot_password(request):
    context = RequestContext(request)
    
    if request.method == "GET":
        form_forgot_password = ForgotPasswordForm()
    else:
        form_forgot_password = ForgotPasswordForm(request.POST)
        if form_forgot_password.validate():
            
            usuario = User.objects.get(email=request.POST.get('email'))

            dashboard_user = DashboardUser.objects.get(user=usuario)
            forgot_password_token = dashboard_user._generate_activation_key()
            dashboard_user.forgot_password_token = forgot_password_token
            dashboard_user.save()
            
            response = _send_forgot_password_email(request, forgot_password_token, dashboard_user)
            errors = form_forgot_password._errors.setdefault(NON_FIELD_ERRORS, ErrorList())
            if response:
                errors.append(u"Something bad happened. Try again, please.")
            else:
                errors.append(u"We sent you an email with instructions.")
        
    
    context.update({'form': form_forgot_password})
    
    return render_to_response('forgot_password.html',
                          context_instance=context)

def _send_forgot_password_email(request, forgot_password_token, dashboard_user):
    try:
        to = dashboard_user.user.email
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = settings.DEFAULT_EMAIL_FORGOT_PASSWORD_SUBJECT
        forgot_password_link = "%s/user/%d/reset-password/token/%s/" % (settings.BASE_URL, dashboard_user.id, forgot_password_token)
        
        body = u"Dear %s," % dashboard_user.user.first_name
        body += u"To update your password access link below:"
        body += u"%s" % forgot_password_link
        body += u"Graciously,"
        body += u"Dashboard Team."
        
        body_html = u"Dear %s,<br /><br />" % dashboard_user.user.first_name
        body_html += u"To update your password access link below:<br /><br />"
        body_html += u"<a href='%s'>%s</a><br /><br />" % (forgot_password_link, forgot_password_link)
        body_html += u"Graciously,<br />"
        body_html += u"Dashboard Team."

        msg = EmailMultiAlternatives(subject, body, from_email, [to])
        msg.attach_alternative(body_html, "text/html")
        msg.send()

    except Exception:
        logging.error("[FORGOT PASSWORD] - sending email failure.")
        return False
    
    return True

def reset_password(request, dashboard_user_id, forgot_password_token):

    context = RequestContext(request)
    context.update({'dashboard_user_id': dashboard_user_id})
    context.update({'forgot_password_token': forgot_password_token})
    
    if request.method == "GET":
        set_password_form = SetPasswordForm()
    else:
        import ipdb;ipdb.set_trace()
        set_password_form = SetPasswordForm(request.POST)
        if set_password_form.validate(dashboard_user_id):
            
            usuario = DashboardUser.objects.get(id=dashboard_user_id)
            usuario.user.set_password(request.POST.get('password'))
            usuario.forgot_password_token = None
            usuario.save()
            usuario.user.save()

            return redirect('dashboard_login')

    context.update({'form': set_password_form})
    return render_to_response('reset_password.html',
                          context_instance=context)

def change_password(request, user_id):
    context = RequestContext(request)
    
    if request.method == "GET":
        change_password_form = ChangePasswordForm()
    else:
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.validate(user_id):
            
            usuario = User.objects.get(id=user_id)
            usuario.set_password(request.POST.get('new_password'))
            usuario.save()

            return redirect('index')

    context.update({'form': change_password_form})
    return render_to_response('change_password.html',
                          context_instance=context)
