# coding: utf-8
import json
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Country

@login_required
def get_triangle_graph_countries(request):
    context = RequestContext(request)
    countries = Country.objects.all()
    return_data = []

    for country in countries:
        dict_country = {
            'country_slug': country.slug,
            'country': country.name,
            'triangle_categories': ["% Avance Tiempo", "Ejecucion Financiera", "Ejecucion Fisica"],
            'series': [
               {'name': 'Ejecución Actual', 'data': [1,2,3], 'pointPlacement': 'on'},
               {'name': 'Ejecución Programada', 'data': [11,22,33], 'pointPlacement': 'on'},
               {'name': 'Ejecución Original Programada', 'data': [1111,2222,3333], 'pointPlacement': 'on'},
               {'name': '$ Comprometido', 'data': [11111,22222,33333], 'pointPlacement': 'on'}
            ]
        }
        return_data.append(dict_country)

    return HttpResponse(json.dumps(return_data), content_type="application/json")
