# coding: utf-8
from core.models import Country


def countries(request):
    countries = {}
    for country in Country.objects.all():
        countries[country.slug] = country
    return {'COUNTRIES': countries}
