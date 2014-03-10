#coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from tables.models import GrantsFinancesOrigin


@login_required
def countries(request):
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
    return render_to_response("countries.html", context)
