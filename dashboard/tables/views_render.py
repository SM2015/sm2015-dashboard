# coding: utf-8
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, UcMilestone, \
        Sm2015Milestone, Objective, GrantsFinances, GrantsFinancesFields

@login_required
def render_hitos(request, country_slug):

    hitos = Hito.objects.filter(country__slug=country_slug, language__acronym=request.LANGUAGE_CODE)
    estados_actuais = EstadoActual.objects.all()
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

    rendered = render_to_string("tables/hitos.html", {
        'hitos': hitos
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_avances_financeiros(request, country_slug):
    avances = AvanceFisicoFinanciero.objects.filter(country__slug=country_slug, language__acronym=request.LANGUAGE_CODE)

    rendered = render_to_string("tables/avances_financeiros.html", {
        'avances': avances,
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_ucmilestone(request):
    ucmilestones = UcMilestone.objects.filter(language__acronym=request.LANGUAGE_CODE)

    rendered = render_to_string("tables/ucmilestone.html", {
        'ucmilestones': ucmilestones,
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_sm2015milestone(request):
    sm2015milestones = Sm2015Milestone.objects.filter(language__acronym=request.LANGUAGE_CODE)

    rendered = render_to_string("tables/sm2015milestone.html", {
        'sm2015milestones': sm2015milestones,
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_grants_finances(request):
    grants_periods = GrantsFinances.objects.values('period').order_by('period')
    grants_fields = GrantsFinancesFields.objects.all().order_by('name')
    table = []
    periods = []

    for row in grants_periods:
        if not row['period'] in periods:
            periods.append(row['period'])

    for field in grants_fields:
        grants_of_field = GrantsFinances.objects.filter(field__id=field.id).order_by('period')
        values = []

        for grant in grants_of_field:
            values.append({
                'value': grant.value,
                'id': grant.id,
                'period': grant.period
            })

        table.append({
            'name': field.name,
            'id': field.id,
            'values': values
        })

    rendered = render_to_string("tables/grants_finances.html", {
        'periods': periods,
        'table': table
    })
    return HttpResponse(rendered, content_type="text/html")
