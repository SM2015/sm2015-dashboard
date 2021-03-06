from django.contrib import admin
from django import forms
from map.models import Map

class MapAdminForm(forms.ModelForm):
    class Meta:
        model = Map

class MapAdmin(admin.ModelAdmin):
    exclude = ('coord',)
    list_display = ('country', 'language')
    form = MapAdminForm

admin.site.register(Map, MapAdmin)
