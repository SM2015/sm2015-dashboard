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
from tables.models import AvanceFisicoFinanciero

@login_required
def index(request):
    maps = Map.objects.all()
    countries_map = []
    for country_map in maps:
        try:
            table_avances = AvanceFisicoFinanciero.objects.get(country=country_map.country)
            variation_physical = table_avances.avance_fisico_planificado - table_avances.avance_fisico_real
            variation_financial = table_avances.avance_financiero_planificado - table_avances.avance_financiero_actual
            if variation_physical <= 25 and variation_financial <= 25:
                pin_color = 'green'
            elif variation_physical >= 25 or variation_financial >= 25:
                pin_color = 'yellow'
            elif variation_physical >= 25 and variation_financial >= 25:
                pin_color = 'red'

            country = {
                'lat': str(country_map.country.latlng.split(',')[0]),
                'lng': str(country_map.country.latlng.split(',')[1]),
                'name': str(country_map.country.name),
                'goal': str(country_map.goal),
                'short_description': str(country_map.short_description),
                'pin_color': pin_color
            }
            countries_map.append(country)
        except AvanceFisicoFinanciero.DoesNotExist:
            continue

    context = RequestContext(request)
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
            
            dashboard_user = DashboardUser.objects.get(user__email=request.POST.get('email'))
            response_email = dashboard_user.send_forgot_password_email()

            if not response_email:
                form_forgot_password.errors.update({'invalid': u"Something bad happened. Try again, please."})
            else:
                form_forgot_password.errors.update({'success': u"We sent you an email with instructions."})
    
    context.update({'form': form_forgot_password})
    
    return render_to_response('forgot_password.html',
                          context_instance=context)

def reset_password(request, forgot_password_token):

    try:
        usuario = DashboardUser.objects.get(forgot_password_token=forgot_password_token)
        context = RequestContext(request)
        context.update({'forgot_password_token': forgot_password_token})
        
        if request.method == "GET":
            set_password_form = SetPasswordForm()
        else:
            set_password_form = SetPasswordForm(request.POST)
            if set_password_form.validate(forgot_password_token):
                usuario.user.set_password(request.POST.get('password'))
                usuario.forgot_password_token = None
                usuario.save()
                usuario.user.save()

                return redirect('dashboard_login')

        context.update({'form': set_password_form})
        return render_to_response('reset_password.html',
                              context_instance=context)

    except DashboardUser.DoesNotExist:
        return redirect('dashboard_login')

@login_required
def change_password(request):
    context = RequestContext(request)
    usuario = context.get('user')
    
    if request.method == "GET":
        change_password_form = ChangePasswordForm()
    else:
        change_password_form = ChangePasswordForm(request.POST)

        if change_password_form.validate(usuario):
            usuario.set_password(request.POST.get('new_password'))
            usuario.save()
            change_password_form.errors.update({'success': u"Password changed!"})

    context.update({'form': change_password_form})
    return render_to_response('change_password.html',
                          context_instance=context)
