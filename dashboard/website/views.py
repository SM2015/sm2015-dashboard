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

from website.forms import LoginForm, SetPasswordForm, ForgotPasswordForm
from core.models import *

@login_required
def index(request):
    context = RequestContext(request)
    context.update({'user_name': context.get('user').first_name})
    logging.info("INFO - sdf")
    logging.error("ERRO - sdf")
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

@login_required
def forgot_password(request):
    context = RequestContext(request)
    
    if request.method == "GET":
        form_forgot_password = ForgotPasswordForm()
    else:
        form_forgot_password = ForgotPasswordForm(request.POST)
        if form_forgot_password.is_valid():
            try:
                usuario = User.objects.get(email=request.POST.get('email'))
                if usuario.is_active:
                    
                    dashboard_user = get_object_or_404(DashboardUser, user=usuario)
                    forgot_password_token = _get_hash(dashboard_user)
                    dashboard_user.forgot_password_token = forgot_password_token
                    dashboard_user.save()
                    
                    response = _send_forgot_password_email(request, forgot_password_token, dashboard_user)

                    if response:
                        messages.error(request, 'We sent you an email with instructions.')
                        context.update({'sent': True})
                    else:
                        messages.error(request, 'Something bad happened. Try again, please.')
                else:
                    context.update({
                        'inactive_user': True,
                        'email': usuario.email
                    })
                    
            except User.DoesNotExist:
                messages.error(request, 'It seems that this email don\'t exists.')
        else:
            messages.error(request, 'That\'s not a valid email.')
    
    context.update({'form': form_forgot_password})           
    
    return render_to_response('forgot_password.html',
                          context_instance=context)

def _send_forgot_password_email(request, forgot_password_token, dashboard_user):
    try:
        to = dashboard_user.user.email
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = settings.DEFAULT_EMAIL_FORGOT_PASSWORD_SUBJECT
        forgot_password_link = "%s/user/%d/reset_password/token/%s/" % (settings.BASE_URL, dashboard_user.id, forgot_password_token)
        
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

@login_required
def reset_password(request, dashboard_user_id, forgot_password_token):
    dashboard_user = get_object_or_404(DashboardUser, id=dashboard_user_id)
    
    if forgot_password_token != dashboard_user.forgot_password_token:
        return redirect("dashboard_login")
    
    context = RequestContext(request)
    reset_password_form = SetPasswordForm()
    
    context.update({
        'form': reset_password_form, 
        'menuchef_user_id':dashboard_user_id, 
        'forgot_password_token':forgot_password_token
        })

    if request.method == "POST":
        password = request.POST.get('password')
        password_conf = request.POST.get('password_conf')
        
        if password == "" or password_conf == "":
            messages.error(request, 'invalid passwords.')
            return render_to_response("reset_password.html", context_instance=context)
            
        if password != password_conf:
            messages.error(request, 'The passwords need to be the same.')
            return render_to_response("reset_password.html", context_instance=context)

        dashboard_user.user.set_password(password)
        dashboard_user.forgot_password_token = None
        dashboard_user.user.save()
        
        dashboard_user.save()
        
        messages.success(request, 'Your password has been updated.')
        return redirect("dashboard_login")
        
    
    return render_to_response("reset_password.html", context_instance=context)

@login_required
def milestone(request):
    milestones = Hito.objects.all()

    context = RequestContext(request)
    
    context.update({
        'milestones': milestones,
    })

    return render_to_response("milestone.html", context_instance=context)

@login_required
def save_milestone_data(request):
    milestone = get_object_or_404(Hito, id=request.POST.get('objid'))
    
    field = request.POST.get('objfield')
    value = request.POST.get('value')

    if field == "indicador_de_pago":
        milestone.indicador_de_pago = value
    elif field == "hito":
        milestone.hito = value
    elif field == "trimestre":
        milestone.trimestre = value
    elif field == "audiencia":
        milestone.audiencia = value
    elif field == "estado_actual":
        milestone.estado_actual = value
    elif field == "alerta_notas":
        milestone.alerta_notas = value
    elif field == "recomendacion":
        milestone.recomendacion = value
    elif field == "acuerdo":
        milestone.acuerdo = value
    elif field == "actividad_en_pod":
        milestone.actividad_en_pod = value

    milestone.save()

    return HttpResponse(value, content_type="application/json")
