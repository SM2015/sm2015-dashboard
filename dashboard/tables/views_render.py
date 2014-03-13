# coding: utf-8
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, UcMilestone, \
        Sm2015Milestone, Objective, GrantsFinances, GrantsFinancesFields, \
        LifeSaveField, LifeSave, CountryOperation, CountryOperationIT


@login_required
def render_hitos(request, country_slug):
    hitos = Hito.objects.filter(country__slug=country_slug, language__acronym=request.LANGUAGE_CODE)
    estados_actuais = EstadoActual.objects.all()
    options_estados_actuais = {}
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
    avances = AvanceFisicoFinanciero.objects \
                                    .filter(country__slug=country_slug,
                                            language__acronym=
                                            request.LANGUAGE_CODE)

    rendered = render_to_string("tables/avances_financeiros.html", {
        'avances': avances,
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_ucmilestone(request, year):
    ucmilestones = UcMilestone.objects \
                              .filter(language__acronym=request.LANGUAGE_CODE) \
                              .filter(date__year=int(year))

    rendered = render_to_string("tables/ucmilestone.html", {
        'ucmilestones': ucmilestones,
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_ucmilestone_noneditable(request, year):
    ucmilestones = UcMilestone.objects \
                              .filter(language__acronym=request.LANGUAGE_CODE) \
                              .filter(date__year=int(year))

    rendered = render_to_string("tables/ucmilestone_noneditable.html", {
        'ucmilestones': ucmilestones,
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_sm2015milestone(request, year):
    sm2015milestones = Sm2015Milestone.objects \
                                      .filter(language__acronym=
                                              request.LANGUAGE_CODE) \
                                      .filter(date__year=int(year))

    rendered = render_to_string("tables/sm2015milestone.html", {
        'sm2015milestones': sm2015milestones
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_sm2015milestone_noneditable(request, year):
    sm2015milestones = Sm2015Milestone.objects \
                        .filter(language__acronym=request.LANGUAGE_CODE) \
                        .filter(date__year=int(year))

    rendered = render_to_string("tables/sm2015milestone_noneditable.html", {
        'sm2015milestones': sm2015milestones
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_grants_finances(request):
    grants_fields = GrantsFinancesFields.objects.all().order_by('name')
    table = []
    periods = GrantsFinances.get_periods()[:14]

    totals = {}
    for period in periods:
        totals.update({"{0}".format(period): {'real': 0, 'expected': 0}})

    for field in grants_fields:
        values = []
        accumulated_value = 0
        for period in periods:
            grant = GrantsFinances.objects.filter(field__id=field.id).filter(quarter__name=period)
            
            if grant:
                accumulated_value += grant[0].value
                values.append({
                    'value': "%.1f" % accumulated_value,
                    'id': grant[0].id,
                    'period': grant[0].quarter.name
                })

                if grant[0].field.field_type.uuid == 'GRANTS_TYPE_REAL':
                    totals[period]['real'] += grant[0].value
                elif grant[0].field.field_type.uuid == 'GRANTS_TYPE_EXPECTED':
                    totals[period]['expected'] += grant[0].value
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

        values_expected.append({'value': "%.1f" % totals[period]['expected']})
        values_real.append({'value': "%.1f" % totals[period]['real']})
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

@login_required
def render_country_operation(request):
    countries = CountryOperation.objects.values('country__name').distinct()
    quarters = CountryOperation.objects.values('quarter__name').order_by('quarter__name').distinct()
    fields = [{'field': 'it_disbursements_planned', 
               'name': 'Planned (PD)',
               'parent_name': 'IT Disbursements'},
             {'field': 'it_disbursements_actual', 
               'name': 'Actual (AD)',
               'parent_name': 'IT Disbursements'},
             {'field': 'it_execution_planned',
               'name': 'Planned (FP)',
               'parent_name': 'IT Execution'},
             {'field': 'it_execution_actual', 
               'name': 'Actual (AE)',
               'parent_name': 'IT Execution'}]

    table = []
    for country in countries:
        country_name = country['country__name']
        operation_it = CountryOperationIT.objects.get(country__name=country_name)
        operation = CountryOperation.objects.filter(country__name=country_name)
        country_rows = []
        for field in fields:
            row = {'field': field,
                   'country': country_name,
                   'it': operation_it.it,
                   'values': []}
            for quarter in quarters:
                quarter_name = quarter['quarter__name']
                operation_quarter = operation.get(quarter__name=quarter_name)
                value = getattr(operation_quarter, field['field'])
                row['values'].append("%.0f" % value)
            country_rows.append(row)
        table.extend(country_rows)

    rendered = render_to_string("tables/country_operation.html", {
        'table': table,
        'quarters': quarters
    })
    return HttpResponse(rendered, content_type="text/html")
