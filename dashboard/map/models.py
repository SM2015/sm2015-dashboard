# coding: utf-8
from django.db import models
from core.models import Country, Language


class Map(models.Model):
    country = models.ForeignKey(Country)
    language = models.ForeignKey(Language, default=1)

    short_description = models.TextField()
    goal = models.IntegerField(default=0, null=True, blank=True)
    more_info_link = models.CharField(max_length=400,
                                      default=None,
                                      null=True,
                                      blank=True)

    def __unicode__(self):
        return self.country.name
