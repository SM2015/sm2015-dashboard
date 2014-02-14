# coding: utf-8
import json
import re
from datetime import datetime
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.db.models import ForeignKey, FieldDoesNotExist, IntegerField, FloatField, DateField
from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, UcMilestone, Sm2015Milestone, Objective, \
        GrantsFinancesOrigin, GrantsFinancesFields, GrantsFinances, GrantsFinancesType, LifeSave, \
        CountryDisbursement
from tables import models as table_models

@login_required
def save_milestone_data(request):
    model_name = request.POST.get('model')
    if not model_name:
        raise Http404

    try:
        value = ""
        class_table = getattr(table_models, model_name)
        instance = get_object_or_404(class_table, id=request.POST.get('objid'))

    except AttributeError, e:
        raise Http404

    for field_name in class_table.get_editable_fields():
        if request.POST.get(field_name, None) != None:
            value = request.POST.get(field_name)
            try:
                field = getattr(class_table, field_name)
                if isinstance(field.field, ForeignKey):
                    instance_related_model = field.field.related.parent_model.objects.get(id=value)
                    setattr(instance, field_name, instance_related_model)
                    value = instance_related_model.name
            except AttributeError, e:
                field = class_table._meta.get_field_by_name(field_name)[0]

                if isinstance(field, IntegerField):
                    real_value = re.sub("\D", "", value)
                elif isinstance(field, FloatField):
                    real_value = re.search('[\d\.\,]+', value).group(0).replace('.', '').replace(',','.')
                elif isinstance(field, DateField):
                    real_value = datetime.strptime(value, "%m/%d/%Y").date()

                    date_str = real_value.strftime("%d de {MONTH} de %Y").lstrip("0")
                    month_translated = _(real_value.strftime("%B"))
                    value = date_str.replace("{MONTH}", month_translated)
                else:
                    real_value = value
                setattr(instance, field_name, real_value)
            except FieldDoesNotExist, e:
                continue
    
    instance.save()

    return HttpResponse(value, content_type="application/json")

@login_required
def hitos_e_avances(request):
    context = RequestContext(request)
    countries = context.get('user').dashboarduser.countries.all()

    context.update({'countries': countries})
    return render_to_response("hitos_e_avances.html", context)

@login_required
def ucmilestone(request):
    context = RequestContext(request)
    return render_to_response("ucmilestone.html", context)

@login_required
def sm2015milestone(request):
    context = RequestContext(request)
    return render_to_response("sm2015milestone.html", context)

@login_required
def grants_finances(request):
    context = RequestContext(request)
    grants_origins = GrantsFinancesOrigin.objects.all()
    origins_values = []
    for origin in grants_origins:
        origins_values.append({
            'uuid': str(origin.uuid),
            'name': str(origin.name),
            'url_ongoing': reverse('grants_finances_ongoing', args=[origin.uuid])
        })

    context.update({'origins': origins_values})
    return render_to_response("grants_finances.html", context)

@login_required
def life_save(request):
    context = RequestContext(request)
    countries = context.get('user').dashboarduser.countries.all()

    context.update({'countries': countries})
    return render_to_response("life_save.html", context)

@login_required
def grants_finances_ongoing(request, uuid_origin):
    try:
        grant_origin = GrantsFinancesOrigin.objects.get(uuid=uuid_origin)
        grant_type_real = GrantsFinancesType.objects.get(uuid='GRANTS_TYPE_REAL')
        grant_type_expected = GrantsFinancesType.objects.get(uuid='GRANTS_TYPE_EXPECTED')
        grant_field_real = GrantsFinancesFields.objects.get(field_origin=grant_origin, field_type=grant_type_real)
        grant_field_expected = GrantsFinancesFields.objects.get(field_origin=grant_origin, field_type=grant_type_expected)

        grants_real = GrantsFinances.objects.filter(field=grant_field_real)
        grants_expected = GrantsFinances.objects.filter(field=grant_field_expected)

        real_accumulated = 0
        expected_accumulated = 0

        for grant in grants_real:
            real_accumulated += grant.value

        for grant in grants_expected:
            expected_accumulated += grant.value

        values = {
            'accumulated': float("%.2f" % (real_accumulated * 1000000)),
            'percentage': float("%.2f" % ((real_accumulated/expected_accumulated) * 100)),
            'dpi': float("%.1f" % (real_accumulated/expected_accumulated)),
            'dv':  float("%.2f" % (expected_accumulated - real_accumulated))
        }

        return HttpResponse(json.dumps(values), content_type="application/json")

    except GrantsFinancesOrigin.DoesNotExist:
        raise Http404

    except GrantsFinancesFields.DoesNotExist:
        raise Http404

@login_required
def chart_flot(request, uuid_type):
    grant_type = GrantsFinancesType.objects.get(uuid=uuid_type)
    grant_fields = GrantsFinancesFields.objects.filter(field_type=grant_type)
    origins = {}
    periods = GrantsFinances.get_periods()

    for field in grant_fields:
        grants = GrantsFinances.objects.filter(field=field)
        accumulated_value = 0
        for grant in grants:
            origin_name = grant.field.field_origin.name
            if not origins.get(origin_name):
                origins.update({"%s" % origin_name: []})
            period = grant.period.replace("Q",".").replace("I", '1').replace("II", '2').replace("III", '3')
            accumulated_value += grant.value
            origins[origin_name].append([float(period), accumulated_value])


    for origin_name in origins:
        periods_is_in = []
        for flot_row in origins[origin_name]:
            period_row = flot_row[0]
            for period in periods:
                period = period.replace("Q",".").replace("I", '1').replace("II", '2').replace("III", '3')
                if float(period) == period_row:
                    periods_is_in.append(period)
        
        for period in periods:
            period = period.replace("Q",".").replace("I", '1').replace("II", '2').replace("III", '3')
            if period not in periods_is_in:
                origins[origin_name].append([float(period), 0])

        # Ordena Origin por periodo
        origins[origin_name].sort(key=lambda x: float(x[0]))

    return HttpResponse(json.dumps(origins), content_type="application/json")

@login_required
def import_excel(request):
    uploaded_file = request.FILES.get('excel')
    app_name = request.POST.get('app_name')

    if app_name == 'tables.grantsfinances':
        GrantsFinances.upload_excel(uploaded_file)
    elif app_name == 'tables.ucmilestone':
        UcMilestone.upload_excel(uploaded_file)
    elif app_name == 'tables.avancefisicofinanciero':
        AvanceFisicoFinanciero.upload_excel(uploaded_file)
    elif app_name == 'tables.hito':
        Hito.upload_excel(uploaded_file)
    elif app_name == 'tables.sm2015milestone':
       Sm2015Milestone.upload_excel(uploaded_file)
    elif app_name == 'tables.lifesave':
       LifeSave.upload_excel(uploaded_file)
    elif app_name == 'tables.countrydisbursement':
       CountryDisbursement.upload_excel(uploaded_file)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
