# coding: utf-8
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from sm2015_calendar.models import Event


@login_required
def index(request):
    context = RequestContext(request)
    events = []

    for event in Event.objects.all():
        event_dict = {
            'title': str(event.name.encode('utf8')),
            'description': str(event.description.encode('utf8')),
            'local': str(event.local.encode('utf8')),
            'start': str(event.start.isoformat()),
            'editable': False,
            'allDay': False
        }

        if event.all_day:
            event_dict['allDay'] = True

        if event.end:
            event_dict['end'] = str(event.end.isoformat())

        events.append(event_dict)

    context.update({'events': json.dumps(events)})
    return render_to_response('calendar.html', context)
