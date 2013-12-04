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

from website.forms import LoginForm, RegisterForm, SetPasswordForm
from core.models import DashboardUser

def index(request):
    return render_to_response('dashboard.html')

def dashboard_login(request):
    context = RequestContext(request)
    
    if request.method == "POST":
        form_login = LoginForm(request.POST)
        if  request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(email=username)
                if user.is_active:
                    if user.check_password(password):
                        user.backend = "django.contrib.auth.backends.ModelBackend"
                        login(request, user)
                        if request.POST.get('remember', None):
                            request.session.set_expiry(0)
                            
                        dashboard_user = DashboardUser.objects.get(user=user)
                        context.update({
                            'dashboard_user': dashboard_user,
                        })
                        return redirect('home')
                    else:
                        form_login.errors.update({'password': [u'incorrect password.']})    
                else:
                    context.update({
                        'inactive_user': True,
                        'email': user.email
                    })
                    form_login.errors.update({'username': [u'inactive user.']})
            except User.DoesNotExist:
                form_login.errors.update({'username': [u'we dont know this email.']})
    else:
        form_login = LoginForm()
    
    register_form = RegisterForm()
    

    context.update({
        'login_form': form_login,
        'register_form': register_form
        })
    return render_to_response('login.html',
                          context_instance=context)

def dashboard_logout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect("dashboard_login")

def register_user(request):
    context = RequestContext(request)
    
    if request.method == "GET":
        register_form = RegisterForm()
        context.update({
            'register_form': register_form,
        })
        
        return render_to_response('register.html', context_instance=context)
    
    else:
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            dashboard_user = register_form.save()

            activation_key = _get_hash(dashboard_user)
            
            dashboard_user.activation_key = activation_key
            dashboard_user.save()
            
            _send_register_confirmation_email(request, activation_key, dashboard_user)

            messages.success(request, 'Just one more step! You need to validate your account. We\'ve just sent you an email.')
            
            context.update({
                'dashboard_user': dashboard_user
                })
            
            return redirect('dashboard_login')
        else:
            context.update({
                'register_form': register_form,
                })
            
    return render_to_response('register.html', context_instance=context)

def _get_hash(instance):
    salt = sha.new(str(random.random())).hexdigest()[:5]
    return sha.new(salt+str(instance.id)).hexdigest()

def _send_register_confirmation_email(request, activation_key, dashboard_user):
    
    try:
        to = dashboard_user.user.email
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = settings.DEFAULT_EMAIL_REGISTER_SUBJECT
        activation_link = "%s/user/activate/?activation_key=%s" % (settings.BASE_URL, activation_key)
        
        body = u"Dear %s," % dashboard_user.user.first_name
        body += u"To confirm your registration visit the link below:"
        body += u"%s" % activation_link
        body += u"Graciously,"
        body += u"Dashboard Team."
        
        body_html = u"Dear %s,<br /><br />" % dashboard_user.user.first_name
        body_html += u"To confirm your registration visit the link below:<br /><br />"
        body_html += u"<a href='%s'>%s</a><br /><br />" % (activation_link, activation_link)
        body_html += u"graciously,<br />"
        body_html += u"Dashboard Team."

        msg = EmailMultiAlternatives(subject, body, from_email, [to])
        msg.attach_alternative(body_html, "text/html")
        msg.send()

    except Exception:
        logging.exception("[registration] - Error sending email.")
        return False


def activate_registered_user(request):
    
    context = RequestContext(request)

    if request.method == "POST":
        activation_key = request.POST.get("activation_key")
        dashboard_user = get_object_or_404(DashboardUser, activation_key=activation_key)

        password = request.POST.get('password')
        password_conf = request.POST.get('password_conf')

        if dashboard_user.user.is_active:
            return redirect("dashboard_login")
        
        if password == "" or password_conf == "":
            messages.error(request, 'invalid passwords.')
            return render_to_response("set_password.html", context_instance=context)
        
        if password != password_conf:
            messages.error(request, 'passwords doesn\'t match.')
            return render_to_response("set_password.html", context_instance=context)
        
        dashboard_user.user.set_password(password)
        dashboard_user.user.is_active = True
        
        dashboard_user.user.save()

        messages.success(request, 'password set!')
        return redirect("dashboard_login")
    else:
        activation_key = request.GET.get("activation_key")

        if not activation_key:
                activation_key = request.POST.get("activation_key")

        dashboard_user = get_object_or_404(DashboardUser, activation_key=activation_key)

        if dashboard_user.user.is_active:
            return redirect("dashboard_login")

        context.update({
            'set_password_form': SetPasswordForm(),
            'activation_key': activation_key,
        })
    
    return render_to_response("set_password.html", context_instance=context)