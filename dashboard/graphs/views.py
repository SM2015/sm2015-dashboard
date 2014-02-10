# coding: utf-8
import json
from datetime import datetime
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Country
from tables.models import AvanceFisicoFinanciero, Operation
from graphs.models import TriangleGraph

@login_required
def get_triangle_graph_countries(request):
    context = RequestContext(request)
    countries = Country.objects.all()
    return_data = []

    for country in countries:
        graph_data = TriangleGraph.get_graph_data_by_country(country=country)
        return_data.append(graph_data)

    return HttpResponse(json.dumps(return_data), content_type="application/json")
