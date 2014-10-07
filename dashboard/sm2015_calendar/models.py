# coding: utf-8
from datetime import datetime
from django.db import models


class Event(models.Model):
    start = models.DateTimeField(null=False, default=datetime.now)
    end = models.DateTimeField(null=True, default=None, blank=True)
    all_day = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=False, default='')
    local = models.CharField(max_length=255, null=True, default=None,
                             blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
