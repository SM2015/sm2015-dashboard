# coding: utf-8
import json
from datetime import datetime
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Country
from tables.models import AvanceFisicoFinanciero, Operation

@login_required
def get_triangle_graph_countries(request):
    context = RequestContext(request)
    countries = Country.objects.all()
    return_data = []

    for country in countries:
        try:
            avances = AvanceFisicoFinanciero.objects.get(country=country)
        except AvanceFisicoFinanciero.DoesNotExist:
            continue

        try: 
            operation = Operation.objects.get(country=country)
            total_days_operation = operation.finish_date - operation.starting_date
            total_days_operation = total_days_operation.days

            total_days_left = operation.finish_date - datetime.date(datetime.today())
            total_days_left = total_days_left.days

            time_remaining = total_days_operation / total_days_left
            avance_tiempo = round(100 - time_remaining, 2)

        except Operation.DoesNotExist:
            avance_tiempo = 0

        financiera = {
            'actual': avances.avance_financiero_actual,
            'programada': avances.avance_financiero_planificado,
            'original_programada': avances.avances_financieros_original_programado,
            'monto_comprometido': avances.monto_comprometido
        }
        fisica = {
            'actual': avances.avance_fisico_real,
            'programada': avances.avance_fisico_planificado,
            'original_programada': avances.avances_fisicos_original_programado,
            'monto_comprometido': avances.monto_comprometido
        }

        dict_country = {
            'country_slug': country.slug,
            'country': country.name,
            'triangle_categories': ["% Avance Tiempo", "Ejecucion Financiera", "Ejecucion Fisica"],
            'series': [
               {'name': 'Ejecución Actual', 'data': [avance_tiempo, financiera.get('actual'), fisica.get('actual')], 'pointPlacement': 'on'},
               {'name': 'Ejecución Programada', 'data': [avance_tiempo, financiera.get('programada'), fisica.get('programada')], 'pointPlacement': 'on'},
               {'name': 'Ejecución Original Programada', 'data': [avance_tiempo, financiera.get('original_programada'), fisica.get('original_programada')], 'pointPlacement': 'on'},
               {'name': '$ Comprometido', 'data': [avance_tiempo, financiera.get('monto_comprometido'), fisica.get('monto_comprometido')], 'pointPlacement': 'on'}
            ]
        }
        return_data.append(dict_country)

    return HttpResponse(json.dumps(return_data), content_type="application/json")
