# coding: utf-8
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Country
from graphs.models import TriangleGraph, LiveSaveGraph, \
    CountryDisbursementGraph


#@login_required
def get_triangle_graph_countries(request):
    country_slug = request.GET.get('country_slug')
    if country_slug:
        countries = Country.objects.filter(slug=country_slug).all()
    else:
        countries = Country.objects.all()
    return_data = []

    for country in countries:
        graph_data = TriangleGraph.get_graph_data_by_country(country=country,
                                                             lang=request.LANGUAGE_CODE)
        return_data.append(graph_data)

    return HttpResponse(json.dumps(return_data),
                        content_type="application/json")


#@login_required
def get_life_save(request, country_slug):
    country = Country.objects.get(slug=country_slug)

    return_data = LiveSaveGraph.get_values_graph(country=country)

    return HttpResponse(json.dumps(return_data),
                        content_type="application/json")


@login_required
def get_country_disbursement(request, country_slug):
    country = Country.objects.get(slug=country_slug)

    return_data = CountryDisbursementGraph.get_values_graph(country=country)

    return HttpResponse(json.dumps(return_data),
                        content_type="application/json")
