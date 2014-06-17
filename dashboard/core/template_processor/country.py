# coding: utf-8
from core.models import Country


def countries(request):
    countries = {}
    countries_dict = {}
    for country in Country.objects.all():
        slug_no_hyphen = country.slug.replace('-', '_')
        countries[slug_no_hyphen] = country

        countries_dict[str(country.slug)] = {}
        countries_dict[str(country.slug)]['name'] = str(country.name)
        countries_dict[str(country.slug)]['slug'] = str(country.slug)
    return {'COUNTRIES': countries, 'COUNTRIES_DICT': countries_dict}
