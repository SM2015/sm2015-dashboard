# coding: utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from tables.models import Hito, AvanceFisicoFinanciero

@login_required
def milestone(request):
    context = RequestContext(request)
    countries = context.get('user').dashboarduser.countries.all()

    hitos = Hito.objects.filter(country__in=countries)
    avances = AvanceFisicoFinanciero.objects.filter(country__in=countries)

    return render_to_response("milestone.html", {
        'context_instance': context,
        'countries': countries,
        'hitos': hitos,
        'avances': avances
    })

@login_required
def save_milestone_data(request):
    milestone = get_object_or_404(Hito, id=request.POST.get('objid'))
    
    field = request.POST.get('objfield')
    value = request.POST.get('value')

    if field == "indicador_de_pago":
        milestone.indicador_de_pago = value
    elif field == "hito":
        milestone.hito = value
    elif field == "trimestre":
        milestone.trimestre = value
    elif field == "audiencia":
        milestone.audiencia = value
    elif field == "estado_actual":
        milestone.estado_actual = value
    elif field == "alerta_notas":
        milestone.alerta_notas = value
    elif field == "recomendacion":
        milestone.recomendacion = value
    elif field == "acuerdo":
        milestone.acuerdo = value
    elif field == "actividad_en_pod":
        milestone.actividad_en_pod = value

    milestone.save()

    return HttpResponse(value, content_type="application/json")
