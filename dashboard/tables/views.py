# coding: utf-8
import json
import re
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.db.models import ForeignKey, FieldDoesNotExist, IntegerField
from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, UcMilestone, Sm2015Milestone, Objective
from tables import models as table_models
from tables.export import ExportDocx

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
                if isinstance(field, IntegerField):
                    value = re.sub("\D", "", value)
                setattr(instance, field_name, value)
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

