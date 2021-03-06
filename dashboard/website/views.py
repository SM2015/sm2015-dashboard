# coding: utf-8


import json
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.clickjacking import xframe_options_exempt

from website.forms import LoginForm, SetPasswordForm, \
    ForgotPasswordForm, ChangePasswordForm
from core.models import *
from map.models import Map
from tables.models import AvanceFisicoFinanciero
from sm2015_calendar.models import Event


# @login_required
def index(request):
    maps = Map.objects.filter(language__acronym=request.LANGUAGE_CODE)
    countries_map = []
    for country_map in maps:
        try:
            table_avances = AvanceFisicoFinanciero.objects \
                .filter(country=country_map.country,
                                            language__acronym=
                                            request.LANGUAGE_CODE).last()



            variation_physical = table_avances.avance_fisico_planificado - table_avances.avance_fisico_real
            variation_financial = table_avances.avance_financiero_planificado - table_avances.avance_financiero_actual
            if variation_physical <= 25 and variation_financial <= 25:
                pin_color = 'green'
            elif variation_physical >= 25 or variation_financial >= 25:
                pin_color = 'yellow'
            elif variation_physical >= 25 and variation_financial >= 25:
                pin_color = 'red'

            if country_map.more_info_link:
                link = country_map.more_info_link.strip().lstrip('/')
                infos_url = "/{0}".format(link)
            else:
                infos_url = "{0}?country={1}&country_slug={2}".format(reverse('country'),
                                                                      country_map.country.id,
                                                                      country_map.country.slug)
            country = {
                'lat': str(country_map.country.latlng.split(',')[0]),
                'lng': str(country_map.country.latlng.split(',')[1]),
                'name': str(country_map.country.name),
                'goal': str(country_map.goal),
                'short_description': unicode(country_map.short_description),
                'pin_color': pin_color,
                'infos_url': infos_url,
                'fecha_actualizacion': table_avances.fecha_de_actualizacion.strftime('%d/%m/%Y')
            }
            countries_map.append(country)
        except (AvanceFisicoFinanciero.DoesNotExist, IndexError, AttributeError):
            continue


    context = RequestContext(request)

    if context.get('user').is_anonymous():
        countries_user = Country.objects.all()
        context.update({'user' : {'is_anonymous': True } })
    else:
        countries_user = context.get('user').dashboarduser.countries.all()
        context.update({'user' : context.get('user') })

    context.update({'countries_map': json.dumps(countries_map)})
    context.update({'countries_user': countries_user})

    events = []

    for event in Event.objects.all():
        event_dict = {
            'title': str(event.name.encode('utf8')),
            'description': str(event.description.encode('utf8')),
            'local': str(event.local.encode('utf8')),
            'start': str(event.start.isoformat()),
            'editable': False,
            'allDay': False
        }

        if event.all_day:
            event_dict['allDay'] = True

        if event.end:
            event_dict['end'] = str(event.end.isoformat())

        events.append(event_dict)
    context.update({'events': json.dumps(events)})

    return render_to_response('index.html', context)


@xframe_options_exempt
@login_required
def index_external(request, language_code):
    context = RequestContext(request)
    context.update({'language_code': language_code})
    return render_to_response('index_external.html',
                              context_instance=context)


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


@xframe_options_exempt
def dashboard_login_external(request, language_code):
    context = RequestContext(request)
    if context.get('user').is_authenticated():
        return redirect('index_external', language_code=language_code)

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
    context.update({'form_login': form_login,
                    'language_code': language_code})
    return render_to_response('login_external.html',
                              context_instance=context)


def dashboard_logout(request):
    context = RequestContext(request)
    context.update({'user' : {'is_anonymous': False } })
    
    if request.user.is_authenticated():
        logout(request)
    return redirect("index")

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


@xframe_options_exempt
def forgot_password_external(request, language_code):
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

    return render_to_response('forgot_password_external.html',
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
