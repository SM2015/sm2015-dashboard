#coding: utf-8
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Country
from tables.models import CountryDetails


@login_required
def countries(request):
    context = RequestContext(request)
    countries = Country.objects.all()
    countries_values = []
    for country in countries:
        countries_values.append({
            'name': str(country.name),
            'url_ongoing': reverse('countries_ongoing', args=[country.slug])
        })

    context.update({'countries': countries_values})
    return render_to_response("countries.html", context)


@login_required
def country_details(request):
    context = RequestContext(request)
    countries = CountryDetails.objects \
                              .values('country__name', 'country__id') \
                              .distinct()
    context.update({'countries': countries})
    return render_to_response("country_details.html", context)


def _get_filter_args_api(request):
    filter_args = []
    if request.GET.get('pago', None) and request.GET.get('pago') != '-1':
        filter_args.append({'pago': request.GET.get('pago')})
    if request.GET.get('isech', None) and request.GET.get('isech') != '-1':
        filter_args.append({'isech': request.GET.get('isech')})
    if request.GET.get('country', None) and request.GET.get('country') != '-1':
        filter_args.append({'country': request.GET.get('country')})
    if request.GET.get('level', None) and request.GET.get('level') != '-1':
        filter_args.append({'level': request.GET.get('level')})
    if request.GET.get('location', None) and request.GET.get('location') != '-1':
        filter_args.append({'location': request.GET.get('location')})
    return filter_args


def _get_obj_filtered_api(request):
    filter_args = _get_filter_args_api(request)
    obj_manager = CountryDetails.objects
    for arg in filter_args:
        obj_manager = obj_manager.filter(**arg)
    return obj_manager


@login_required
def api_list_location(request):
    obj_manager = _get_obj_filtered_api(request)
    values = obj_manager.values('location').distinct()
    values = [l['location'] for l in values]
    return HttpResponse(json.dumps(values), content_type="application/json")


@login_required
def api_list_isech(request):
    obj_manager = _get_obj_filtered_api(request)
    values = obj_manager.values('isech__name', 'isech__id').distinct()
    values = [{'name': v.get('isech__name'), 'id': v.get('isech__id')} for v in values]
    return HttpResponse(json.dumps(values), content_type="application/json")


@login_required
def api_list_pago(request):
    obj_manager = _get_obj_filtered_api(request)
    values = obj_manager.values('pago__name', 'pago__id').distinct()
    values = [{'name': v.get('pago__name'), 'id': v.get('pago__id')} for v in values]
    return HttpResponse(json.dumps(values), content_type="application/json")


@login_required
def api_list_level(request):
    obj_manager = _get_obj_filtered_api(request)
    values = obj_manager.values('level__name', 'level__id').distinct()
    values = [{'name': v.get('level__name'), 'id': v.get('level__id')} for v in values]
    return HttpResponse(json.dumps(values), content_type="application/json")
