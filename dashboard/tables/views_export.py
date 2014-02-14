# coding: utf-8
import codecs
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse
from django.template import RequestContext
from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, Operation
from graphs.models import TriangleGraph
from core.models import Country

@login_required
def render_export_hitos_and_avances(request, country_slug):
    context = RequestContext(request)
    hitos = Hito.objects.filter(country__slug=country_slug)
    estados_actuais = EstadoActual.objects.all()
    country = Country.objects.get(slug=country_slug)
    options_estados_actuais = {}
    hitos_estados_actuais = {}
    for estado in estados_actuais:
        options_estados_actuais.update({
            "{id}".format(id=estado.id): str(estado.name)
        })

    for hito in hitos:
        options_estados_actuais.update({
            'selected': str(hito.estado_actual.id)
        })
        hito.options_estados_actuais = options_estados_actuais

    avances = AvanceFisicoFinanciero.objects.filter(country=country)

    context.update({'hitos': hitos})
    context.update({'avances': avances})
    context.update({'operation': Operation.objects.get(country=country)})

    rendered = render_to_string("tables/word/hitos_and_avances.html", context)

    response = HttpResponse(mimetype='text/html')
    response['Content-Disposition'] = 'attachment; filename={country_slug}_hitos_y_avances.docx'.format(country_slug=country_slug)
    response['Content-Encoding'] = 'UTF-8'
    response['Content-type'] = 'text/html; charset=UTF-8'
    response.write(rendered.encode('utf8'))
    return response
