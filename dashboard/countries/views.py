#coding: utf-8
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from map.models import Map
from core.models import Country
from tables.models import CountryDetails, CountryDetailsValues, \
    AvanceFisicoFinanciero, Operation, OperationInfos


#@login_required
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

    if context.get('user').is_anonymous():
        countries_user = Country.objects.all()
        context.update({'user' : {'is_anonymous': True } })
    else:
        countries = context.get('user').dashboarduser.countries.all()
        context.update({'user' : context.get('user') })

    context.update({'countries': countries})
    return render_to_response("countries.html", context)


@login_required
def country_details(request):
    context = RequestContext(request)
    countries = CountryDetails.objects \
                              .values('country__name', 'country__id') \
                              .distinct()
    context.update({'countries': countries})
    return render_to_response("country_details.html", context)


#@login_required
def country(request):
    context = RequestContext(request)
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
                infos_url = "{0}?country={1}".format(reverse('country_details'),
                                                     country_map.country.id)

            operations = Operation.objects.filter(country__slug=country_map.country.slug)
            if request.GET.get('operation'):
                try:
                    operation = operations.get(number=request.GET.get('operation'))
                except Operation.DoesNotExist:
                    operation = operations.last()
            else:
                operation = operations.last()

            country = {
                'lat': str(country_map.country.latlng.split(',')[0]),
                'lng': str(country_map.country.latlng.split(',')[1]),
                'name': str(country_map.country.name),
                'slug': str(country_map.country.slug),
                'goal': str(country_map.goal),
                'short_description': unicode(country_map.short_description),
                'pin_color': pin_color,
                'infos_url': infos_url,
                'operation': {
                    'name': operation.name,
                    'number': operation.number,
                    'executing_agency': operation.executing_agency,
                    'benefitted_population': operation.benefitted_population,
                    'starting_date': operation.starting_date.strftime('%B %d, %Y'),
                    'zones': []
                }
            }

            for zone in operation.operationzones_set.all():
                zone_dict = {
                    'name': zone.name,
                    'lat': zone.latlng.split(',')[0],
                    'lng': zone.latlng.split(',')[1]
                }
                country['operation']['zones'].append(zone_dict)

            countries_map.append(country)
        except (AvanceFisicoFinanciero.DoesNotExist, IndexError, AttributeError):
            continue

    context.update({'countries_map': json.dumps(countries_map)})

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

        operations = Operation.objects.filter(country__slug=country.slug)
        import ipdb;ipdb.set_trace()
        if request.GET.get('operation'):
            try:
                operation = operations.get(number=request.GET.get('operation'))
            except Operation.DoesNotExist:
                operation = operations.last()
        else:
            operation = operations.last()

        operation_infos = OperationInfos.objects \
                                        .filter(language__acronym=request.LANGUAGE_CODE) \
                                        .filter(operation=operation)

        if operation_infos:
            operation_infos = operation_infos[0]
        else:
            operation_infos = None
        context.update({
                        'country_disbursement': country_disbursement_values,
                        'country_execution': country_execution_values,
                        'operation': operation,
                        'operation_infos': operation_infos,
                        'operations': operations
                        })

    context.update({'countries': countries})
    return render_to_response("country.html", context)


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
