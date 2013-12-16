# coding: utf-8
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.db.models import ForeignKey, FieldDoesNotExist
from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, UcMilestone, Sm2015Milestone, Objective
from tables import models as table_models


@login_required
def milestone(request):
    context = RequestContext(request)

    countries = context.get('user').dashboarduser.countries.all()
    tables = []

    for country in countries:
        table = {
            'country': country,
            'hitos': Hito.objects.filter(country=country),
            'avances': AvanceFisicoFinanciero.objects.filter(country=country),
        }
        tables.append(table)

    return render_to_response("milestone.html", {
        'context_instance': context,
        'countries': countries,
        'tables': tables,
        'user_name': context.get('user').first_name,
        'csrf_token': csrf(request)
    })

@login_required
def save_milestone_data(request, model_name):
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
                setattr(instance, field_name, value)
            except FieldDoesNotExist, e:
                continue
    
    instance.save()

    return HttpResponse(value, content_type="application/json")

@login_required
def list_estado_actual(request):
    estados_actuais = EstadoActual.objects.all()
    list_estados = []
    for estado in estados_actuais:
        list_estados.append({
            'name': estado.name,
            'id': estado.id
        })
    return HttpResponse(json.dumps(list_estados), content_type="application/json")

@login_required
def render_hitos(request, country_slug):
    hitos = Hito.objects.filter(country__slug=country_slug)
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
def render_ucmilestone(request):
    ucmilestones = UcMilestone.objects.all()

    rendered = render_to_string("tables/ucmilestone.html", {
        'ucmilestones': ucmilestones
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_sm2015milestone(request):
    sm2015milestones = Sm2015Milestone.objects.all()

    rendered = render_to_string("tables/sm2015milestone.html", {
        'sm2015milestones': sm2015milestones
    })
    return HttpResponse(rendered, content_type="text/html")