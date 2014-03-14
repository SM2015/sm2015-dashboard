#coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from core.models import Country


@login_required
def countries(request):
    context = RequestContext(request)
    countries = Country.objects.all()
    countries_values = []
    for country in countries:
        countries_values.append({
            'name': str(country.name),
            'url_ongoing': reverse('countries_ongoing', args=[country.slug])
        })

    context.update({'countries': countries_values})
    return render_to_response("countries.html", context)


@login_required
def country_details(request):
    context = RequestContext(request)

    return render_to_response("country_details.html", context)
