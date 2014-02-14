# coding: utf-8
import json
from django.http import HttpResponse
from core.models import Country

def list_country(request):
    countries = Country.objects.all()
    data = []
    for country in countries:
        data.append({
            'name': country.name,
            'slug': country.slug,
            'latlgn': country.latlng
        })
    return HttpResponse(json.dumps(data), content_type="application/json")
