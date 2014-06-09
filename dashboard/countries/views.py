#coding: utf-8
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Country
from tables.models import CountryDetails, CountryDetailsValues


@login_required
def countries(request):
    context = RequestContext(request)
    countries = Country.objects.all()
    countries_disbursement_values = []
    countries_execution_values = []

    for country in countries:
        countries_disbursement_values.append({
            'name': str(country.name),
            'url_ongoing': reverse('countries_ongoing', args=[country.slug, 'disbursement'])
        })
        countries_execution_values.append({
            'name': str(country.name),
            'url_ongoing': reverse('countries_ongoing', args=[country.slug, 'execution'])
        })

    context.update({'countries_disbursement': countries_disbursement_values,
                    'countries_execution': countries_execution_values})

    countries = context.get('user').dashboarduser.countries.all()
    context.update({'countries': countries})
    return render_to_response("countries.html", context)


@login_required
def country_details(request):
    context = RequestContext(request)
    countries = CountryDetails.objects \
                              .values('country__name', 'country__id') \
                              .distinct()

    country_requested = request.GET.get('country_slug')
    if country_requested:
        country = Country.objects.get(slug=country_requested)
        country_disbursement_values = {
            'name': str(country.name),
            'url_ongoing': reverse('countries_ongoing', args=[country.slug, 'disbursement'])
        }
        country_execution_values = {
            'name': str(country.name),
            'url_ongoing': reverse('countries_ongoing', args=[country.slug, 'execution'])
        }

        context.update({'country_disbursement': country_disbursement_values,
                        'country_execution': country_execution_values})

    context.update({'countries': countries})
    return render_to_response("country_details.html", context)


def _get_filter_args_api(request):
    filter_args = []
    if request.GET.getlist('pago', None) and request.GET.getlist('pago') != ['-1']:
        filter_args.append({'pago__in': request.GET.getlist('pago')})
    if request.GET.getlist('isech', None) and request.GET.getlist('isech') != ['-1']:
        filter_args.append({'isech__in': request.GET.getlist('isech')})
    if request.GET.get('country', None) and request.GET.get('country') != '-1':
        filter_args.append({'country': request.GET.get('country')})
    if request.GET.get('level', None) and request.GET.get('level') != '-1':
        filter_args.append({'level': request.GET.get('level')})
    if request.GET.get('location', None) and request.GET.get('location') != '-1':
        filter_args.append({'location': request.GET.get('location')})
    if request.GET.getlist('quarter', None) and request.GET.getlist('quarter') != '-1':
        filter_args.append({'countrydetailsvalues__quarter__in': request.GET.getlist('quarter')})
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


@login_required
def api_list_quarter(request):
    obj_manager = _get_obj_filtered_api(request)
    country_details = obj_manager.all()
    values = CountryDetailsValues.objects \
                                 .filter(country_detail=country_details) \
                                 .values("quarter__name", "quarter__id") \
                                 .distinct()

    values = [{'name': v.get('quarter__name'), 'id': v.get('quarter__id')} for v in values]
    return HttpResponse(json.dumps(values), content_type="application/json")
