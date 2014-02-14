# coding: utf-8
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, UcMilestone, \
        Sm2015Milestone, Objective, GrantsFinances, GrantsFinancesFields, \
        LifeSaveField, LifeSave

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
    grants_fields = GrantsFinancesFields.objects.all().order_by('name')
    table = []
    periods = GrantsFinances.get_periods()

    totals = {}
    for period in periods:
        totals.update({"{0}".format(period): {'real': 0, 'expected': 0}})

    for field in grants_fields:
        values = []
        accumulated_value = 0
        for period in periods:
            grant = GrantsFinances.objects.filter(field__id=field.id).filter(period=period)
            
            if grant:
                accumulated_value += grant[0].value
                values.append({
                    'value': accumulated_value,
                    'id': grant[0].id,
                    'period': grant[0].period
                })

                if grant[0].field.field_type.uuid == 'GRANTS_TYPE_REAL':
                    totals[period]['real'] += accumulated_value
                elif grant[0].field.field_type.uuid == 'GRANTS_TYPE_EXPECTED':
                    totals[period]['expected'] += accumulated_value
            else:
                values.append({
                    'value': '',
                    'id': '',
                    'period': ''
                })

        table.append({
            'name': field.name,
            'id': field.id,
            'values': values
        })

    values_expected = []
    values_real = []
    period_before = None
    for period in periods:
        if period_before:
            totals[period]['expected'] += totals[period_before]['expected']
            totals[period]['real'] += totals[period_before]['real']

        values_expected.append({'value': totals[period]['expected']})
        values_real.append({'value': totals[period]['real']})
        period_before = period

    table.append({'name': 'Total Expected Donors Inflow', 'values': values_expected, 'highlight': True})
    table.append({'name': 'Total Cummulative Donors Inflow', 'values': values_real, 'highlight': True})

    rendered = render_to_string("tables/grants_finances.html", {
        'periods': periods,
        'table': table,
        'totals': totals
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_life_save(request, country_slug):
    fields = LifeSaveField.objects.all().order_by('name')
    table = []

    for field in fields:
        life_save = LifeSave.objects.filter(field__id=field.id).filter(country__slug=country_slug)

        if life_save:
            life_save = life_save[0]

            table.append([
                {'value': field.name, 'id': field.id, 'model': 'LifeSaveField', 'name':'name'},
                {'value': field.abbr, 'id': field.id, 'model': 'LifeSaveField', 'name':'abbr'},
                {'value': life_save.percentage, 'id': life_save.id, 'model': 'LifeSave', 'name':'percentage'},
                {'value': life_save.number_saving, 'id': life_save.id, 'model': 'LifeSave', 'name':'number_saving'}
            ])

    rendered = render_to_string("tables/life_save.html", {
        'table': table,
    })
    return HttpResponse(rendered, content_type="text/html")
