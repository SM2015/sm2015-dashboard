# coding: utf-8
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, UcMilestone, \
        Sm2015Milestone, Objective, GrantsFinances

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
def render_avances_financeiros(request, country_slug):
    avances = AvanceFisicoFinanciero.objects.filter(country__slug=country_slug)

    rendered = render_to_string("tables/avances_financeiros.html", {
        'avances': avances,
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_ucmilestone(request):
    ucmilestones = UcMilestone.objects.all()

    rendered = render_to_string("tables/ucmilestone.html", {
        'ucmilestones': ucmilestones,
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_sm2015milestone(request):
    sm2015milestones = Sm2015Milestone.objects.all()

    rendered = render_to_string("tables/sm2015milestone.html", {
        'sm2015milestones': sm2015milestones,
    })
    return HttpResponse(rendered, content_type="text/html")

@login_required
def render_grants_finances(request):
    grants_finances = GrantsFinances.objects.all()

    table = {
        'contribution_accumulated_bmgf': [],
        'contribution_accumulated_icss': [],
        'contribution_spanish_government': [],
        'korean_tc_accumulated': [],
        'contribution_donates': [],
        'contribution_real_bmgf': [],
        'contribution_real_icss': [],
        'contribution_real_gos': [],
        'korea_actual': []
    }

    for obj in grants_finances:
        for field in table.keys():
            table[field].append(getattr(obj, field))

    rendered = render_to_string("tables/grants_finances.html", {
        'grants_finances': grants_finances,
        'table': table
    })
    return HttpResponse(rendered, content_type="text/html")
