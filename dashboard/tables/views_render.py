# coding: utf-8
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, \
    UcMilestone, Sm2015Milestone, GrantsFinances, \
    GrantsFinancesFields, LifeSaveField, LifeSave, \
    CountryOperation, CountryDetails, \
    CountryDetailsValues, Quarter, Operation, OperationTotalInvestment, \
    CountryRiskIdentification, CountryMainRisks, CountryRiskLevels, \
    CountryRiskIdentificationFields
from core.models import Country
from countries.views import _get_obj_filtered_api


@login_required
def render_hitos(request, country_slug):
    if country_slug in ['belize']:
        language_code = 'en'
    else:
        language_code = 'es'

    hitos = Hito.objects.filter(country__slug=country_slug,
                                language__acronym=language_code)
    estados_actuais = EstadoActual.objects.all()
    options_estados_actuais = {}
    for estado in estados_actuais:
        options_estados_actuais.update({
            "{id}".format(id=estado.id): str(estado.name)
        })

    for hito in hitos:
        if hito.estado_actual:
            option = {
                'selected': str(hito.estado_actual.id)
            }
        options_estados_actuais.update(option)
        hito.options_estados_actuais = options_estados_actuais

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_HITOS'
    )

    rendered = render_to_string("tables/hitos.html", {
        'hitos': hitos,
        'editable': can_edit
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_hitos_noneditable(request, country_slug):
    hitos = Hito.objects.filter(country__slug=country_slug,
                                language__acronym=request.LANGUAGE_CODE)
    estados_actuais = EstadoActual.objects.all()
    options_estados_actuais = {}
    for estado in estados_actuais:
        options_estados_actuais.update({
            "{id}".format(id=estado.id): str(estado.name)
        })

    for hito in hitos:
        if hito.estado_actual:
            option = {
                'selected': str(hito.estado_actual.id)
            }
        options_estados_actuais.update(option)
        hito.options_estados_actuais = options_estados_actuais

    rendered = render_to_string("tables/hitos_noneditable.html", {
        'hitos': hitos,
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_avances_financeiros(request, country_slug):
    avance = AvanceFisicoFinanciero.objects \
                                   .filter(country__slug=country_slug,
                                           language__acronym=
                                           request.LANGUAGE_CODE).last()

    if avance and not avance.upcoming_policy_dialogue_events:
        avance.upcoming_policy_dialogue_events = ''

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_AVANCE_FISICO_FINANCIEROS'
    )

    rendered = render_to_string("tables/avances_financeiros.html", {
        'avance': avance,
        'editable': can_edit
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_ucmilestone(request, year):
    ucmilestones = UcMilestone.objects \
                              .filter(language__acronym=request.LANGUAGE_CODE)

    ucmilestones = Quarter.filter_objects_by_year(ucmilestones, year)

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_UC_MILESTONES'
    )

    rendered = render_to_string("tables/ucmilestone.html", {
        'ucmilestones': ucmilestones,
        'editable': can_edit
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_ucmilestone_noneditable(request, year):
    ucmilestones = UcMilestone.objects \
                              .filter(language__acronym=request.LANGUAGE_CODE)

    ucmilestones = Quarter.filter_objects_by_year(ucmilestones, year)

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

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_SM2015_MILESTONES'
    )

    rendered = render_to_string("tables/sm2015milestone.html", {
        'sm2015milestones': sm2015milestones,
        'editable': can_edit
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


def _get_grants_finances_table(request):
    grants_fields = GrantsFinancesFields.objects.all().order_by('name')
    table = []
    periods = GrantsFinances.get_periods_until_now(14)

    totals = {}
    for period in periods:
        totals.update({"{0}".format(period): {'real': 0, 'expected': 0}})

    for field in grants_fields:
        values = []
        for period in periods:
            grant = GrantsFinances.objects \
                                  .filter(field__id=field.id) \
                                  .filter(quarter__name=period)

            if grant:
                values.append({
                    'value': "%.1f" % grant[0].value,
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
    for period in periods:
        values_expected.append({'value': "%.1f" % totals[period]['expected']})
        values_real.append({'value': "%.1f" % totals[period]['real']})

    table.append({'name': 'Total Expected Donors Inflow',
                  'values': values_expected,
                  'highlight': True})
    table.append({'name': 'Total Cummulative Donors Inflow',
                  'values': values_real,
                  'highlight': True})

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_GRANTS_FINANCES'
    )
    return {
        'periods': periods,
        'table': table,
        'totals': totals,
        'editable': can_edit
    }


@login_required
def render_grants_finances(request):
    context = _get_grants_finances_table(request)
    rendered = render_to_string("tables/grants_finances.html", context)
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_grants_finances_noneditable(request):
    context = _get_grants_finances_table(request)
    rendered = render_to_string("tables/grants_finances_noneditable.html",
                                context)
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

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_LISTS'
    )

    rendered = render_to_string("tables/life_save.html", {
        'table': table,
        'editable': can_edit
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_country_operation(request):
    until_actual_quarter = request.GET.get('until_actual_quarter', None)
    if until_actual_quarter:
        actual_quarter = Quarter.get_actual_quarter()
        table, quarters, total = CountryOperation.get_table_to_show(with_total=True,
                                                                    until_quarter=actual_quarter)
    else:
        table, quarters, total = CountryOperation.get_table_to_show(with_total=True)

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_COUNTRY_OPERATION'
    )

    rendered = render_to_string("tables/country_operation.html", {
        'table': table,
        'quarters': quarters,
        'total': total,
        'editable': can_edit
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_country_operation_noneditable(request):
    until_actual_quarter = request.GET.get('until_actual_quarter', None)
    if until_actual_quarter:
        actual_quarter = Quarter.get_actual_quarter()
        table, quarters, total = CountryOperation.get_table_to_show(with_total=True,
                                                                    until_quarter=actual_quarter)
    else:
        table, quarters, total = CountryOperation.get_table_to_show(with_total=True)

    rendered = render_to_string("tables/country_operation_noneditable.html", {
        'table': table,
        'quarters': quarters,
        'total': total
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_country_details(request):
    country_details = _get_obj_filtered_api(request)
    table = []
    periods = CountryDetails.get_periods(country_details)

    for country_detail in country_details.all():
        row_values = []
        for period in periods:
            values = []
            country_values = CountryDetailsValues.objects \
                                                 .filter(country_detail=country_detail) \
                                                 .filter(quarter__name=period)

            if country_values:
                values = country_values[0]
                field_values = {}
                field_values['id'] = values.id
                field_values['numerador_value'] = values.numerador_reportado or ''
                field_values['denominador_value'] = values.denominador_reportado or ''
                if values.numerador_reportado and values.denominador_reportado:
                    field_values['percentage'] = values.numerador_reportado/values.denominador_reportado
                else:
                    field_values['percentage'] = ''
            else:
                field_values['id'] = ''
                field_values['numerador_value'] = ''
                field_values['denominador_value'] = ''
                field_values['percentage'] = ''

            row_values.append(field_values)

        table.append({
            'pago': country_detail.pago,
            'isech': country_detail.isech,
            'level': country_detail.level,
            'location': country_detail.location,
            'values': row_values
        })

    can_edit = request.user.dashboarduser.can_edit_table(
        uuid_table_edit_access='TABLE_EDIT_ACCESS_COUNTRY_DETAILS'
    )

    rendered = render_to_string("tables/country_details.html", {
        'periods': periods,
        'table': table,
        'editable': can_edit
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_operation_total_investment(request, country_slug):
    country = Country.objects.get(slug=country_slug)
    operation = Operation.objects.get(country=country)
    rows = OperationTotalInvestment.objects.get(operation=operation)

    table = [
        ['Investment tranche',
         rows.investment_tranche_first_operation,
         rows.investment_tranche_second_operation],
        ['Counterpart tranche',
         rows.counterpart_tranche_first_operation,
         rows.counterpart_tranche_second_operation],
        ['Cost of the Operation',
         rows.cost_of_the_operation_first_operation,
         rows.cost_of_the_operation_second_operation],
        ['Performance tranche*',
         rows.performance_tranche_first_operation,
         rows.performance_tranche_second_operation],
    ]

    if rows.investment_tranche_third_operation:
        table[0].append(rows.investment_tranche_third_operation)
        table[1].append(rows.counterpart_tranche_third_operation)
        table[2].append(rows.cost_of_the_operation_third_operation)
        table[3].append(rows.performance_tranche_third_operation)

    table[0].append(rows.investment_tranche_first_operation + rows.investment_tranche_second_operation + rows.investment_tranche_third_operation)
    table[1].append(rows.counterpart_tranche_first_operation + rows.counterpart_tranche_second_operation + rows.counterpart_tranche_third_operation)
    table[2].append(rows.cost_of_the_operation_first_operation + rows.cost_of_the_operation_second_operation + rows.cost_of_the_operation_third_operation)
    table[3].append(rows.performance_tranche_first_operation + rows.performance_tranche_second_operation + rows.performance_tranche_third_operation)

    total = ['Total',
             rows.cost_of_the_operation_first_operation +
             rows.performance_tranche_first_operation,

             rows.cost_of_the_operation_second_operation +
             rows.performance_tranche_second_operation]

    if rows.investment_tranche_third_operation:
        total.append(rows.cost_of_the_operation_third_operation +
                     rows.performance_tranche_third_operation)

    total.append(rows.cost_of_the_operation_first_operation + rows.cost_of_the_operation_second_operation + rows.cost_of_the_operation_third_operation +
    rows.performance_tranche_first_operation + rows.performance_tranche_second_operation + rows.performance_tranche_third_operation)

    rendered = render_to_string("tables/operation_total_investment.html", {
        'table': table,
        'total': total,
        'rows': rows,
        'country': country
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_country_risk_identification(request, country_slug):
    country = Country.objects.get(slug=country_slug)
    fields = CountryRiskIdentification.objects.filter(country=country)

    table = {'POSITIVE': [],
             'NEGATIVE': []}

    total = {'POSITIVE': {'total': 0},
             'NEGATIVE': {'total': 0}}

    for table_type in table:

        fields_index_map = {}
        fields_list = []

        for field in fields.filter(type__uuid=table_type):
            field_list_index = fields_index_map.get(field.field.uuid)

            if field_list_index is None:
                field_dict = {
                    'name': field.field.name,
                    'level': {'total': 0}
                }
            else:
                field_dict = fields_list[field_list_index]

            for level in CountryRiskLevels.objects.all():
                if not field_dict['level'].get(level.uuid.lower()):
                    field_value = fields.filter(level=level, type__uuid=table_type, field__uuid=field.field.uuid)
                    if field_value:
                        field_dict['level'][level.uuid.lower()] = field_value[0].value
                        field_dict['level']['total'] += field_value[0].value

                        if total[table_type].get(level.uuid.lower()):
                            total[table_type][level.uuid.lower()] += field_value[0].value
                        else:
                            total[table_type][level.uuid.lower()] = field_value[0].value
                        total[table_type]['total'] += field_value[0].value
                    else:
                        field_dict['level'][level.uuid.lower()] = ''

            if field_list_index is None:
                field_list_index = len(fields_list)
                fields_index_map[field.field.uuid] = field_list_index
                fields_list.append(field_dict)
            else:
                fields_list[field_list_index] = field_dict

        table[table_type].extend(fields_list)

    if request.LANGUAGE_CODE == 'es':
        for type in table:
            for row in table[type]:
                if row['name'] == 'Quality':
                    row['name'] = 'Calidad'
                elif row['name'] == 'Context':
                    row['name'] = 'Contexto'
                elif row['name'] == 'Strategic':
                    row['name'] = 'Estrategicos'
                elif row['name'] == 'Financial':
                    row['name'] = 'Financieros'
                elif row['name'] == 'Stakeholders':
                    row['name'] = 'Interesados'
                elif row['name'] == 'Institutional Leadership':
                    row['name'] = 'Liderazgo institucional'
                elif row['name'] == 'Operational':
                    row['name'] = 'Operacional'
                elif row['name'] == 'Social and Environmental':
                    row['name'] = 'Sociales y Ambientales'
                elif row['name'] == 'Sustainability':
                    row['name'] = 'Sostenibilidad'

    rendered = render_to_string("tables/country_risk_identification.html", {
        'table': table,
        'country': country,
        'total': total
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_country_risk_top(request, country_slug):
    country = Country.objects.get(slug=country_slug)
    rows = CountryMainRisks.objects.filter(country=country,
                                           language__acronym=request.LANGUAGE_CODE)

    table = {'positives': [r for r in rows.filter(type__uuid='POSITIVE')],
             'negatives': [r for r in rows.filter(type__uuid='NEGATIVE')]}

    if request.LANGUAGE_CODE == 'es':
        for type in table:
            for row in table[type]:
                if row.level.uuid == 'VERY_HIGH':
                    row.level.name = 'Muy Alto'
                elif row.level.uuid == 'HIGH':
                    row.level.name = 'Alto'
                elif row.level.uuid == 'MEDIUM':
                    row.level.name = 'Medio'
                elif row.level.uuid == 'LOW':
                    row.level.name = 'Bajo'

    rendered = render_to_string("tables/country_risk_top.html", {
        'table': table,
        'country': country
    })
    return HttpResponse(rendered, content_type="text/html")


@login_required
def render_country_risk_causes(request):
    fields = CountryRiskIdentificationFields.objects.all()
    table = []
    total = {'total': 0}

    for field in fields:
        field_dict = {
            'name': field.name,
            'level': {'total': 0}
        }
        for level in CountryRiskLevels.objects.all():
            field_level = CountryRiskIdentification.objects.filter(level=level,
                                                                   field=field)
            for identification in field_level:
                if field_dict['level'].get(level.uuid.lower()):
                    field_dict['level'][level.uuid.lower()] += identification.value
                else:
                    field_dict['level'][level.uuid.lower()] = identification.value

                field_dict['level']['total'] += identification.value

                if total.get(level.uuid.lower()):
                    total[level.uuid.lower()] += identification.value
                else:
                    total[level.uuid.lower()] = identification.value

                total['total'] += identification.value

        table.append(field_dict)

    total_percentage = float(total.get('total')) / 100
    for row in table:
        for level_uuid in row.get('level'):
            value = float(row['level'][level_uuid])
            row['level'][level_uuid] = "%0.f" % (value / total_percentage)

    for level_uuid in total:
        value = float(total[level_uuid])
        total[level_uuid] = "%0.f" % (value / total_percentage)

    if request.LANGUAGE_CODE == 'es':
        for row in table:
            if row['name'] == 'Quality':
                row['name'] = 'Calidad'
            elif row['name'] == 'Context':
                row['name'] = 'Contexto'
            elif row['name'] == 'Strategic':
                row['name'] = 'Estrategicos'
            elif row['name'] == 'Financial':
                row['name'] = 'Financieros'
            elif row['name'] == 'Stakeholders':
                row['name'] = 'Interesados'
            elif row['name'] == 'Institutional Leadership':
                row['name'] = 'Liderazgo institucional'
            elif row['name'] == 'Operational':
                row['name'] = 'Operacional'
            elif row['name'] == 'Social and Environmental':
                row['name'] = 'Sociales y Ambientales'
            elif row['name'] == 'Sustainability':
                row['name'] = 'Sostenibilidad'

    rendered = render_to_string("tables/country_risk_causes.html", {
        'table': table,
        'total': total
    })

    return HttpResponse(rendered, content_type="text/html")
