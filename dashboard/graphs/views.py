# coding: utf-8
import json
from datetime import datetime
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Country
from tables.models import AvanceFisicoFinanciero, Operation, LifeSave
from graphs.models import TriangleGraph, LiveSaveGraph

@login_required
def get_triangle_graph_countries(request):
    context = RequestContext(request)
    countries = Country.objects.all()
    return_data = []

    for country in countries:
        graph_data = TriangleGraph.get_graph_data_by_country(country=country)
        return_data.append(graph_data)

    return HttpResponse(json.dumps(return_data), content_type="application/json")

@login_required
def get_life_save(request, country_slug):
    context = RequestContext(request)
    country = Country.objects.get(slug=country_slug)
    
    return_data = LiveSaveGraph.get_values_graph(country=country)

    return HttpResponse(json.dumps(return_data), content_type="application/json")
