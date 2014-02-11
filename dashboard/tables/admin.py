# coding: utf-8
from django.contrib import admin
from django.forms import ModelForm
from django.conf.urls import patterns
from tables.models import AvanceFisicoFinanciero, Hito, UcMilestone, \
        Sm2015Milestone, Objective, GrantsFinances, GrantsFinancesFields, Operation, \
        LifeSave, LifeSaveField

class HitoAdmin(admin.ModelAdmin):
    list_display = ('country', 'indicador_de_pago')
    change_list_template = 'change_list.html'

class GrantsFinancesAdmin(admin.ModelAdmin):
    list_display = ('period', 'field')
    change_list_template = 'change_list.html'

class UcMilestoneAdmin(admin.ModelAdmin):
    list_display = ('coordination_unit_milestone', 'quarter', 'language',)
    change_list_template = 'change_list.html'

class AvanceFisicoFinancieroAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'

class Sm2015MilestoneAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'

class LifeSaveAdmin(admin.ModelAdmin):
    list_display = ('country', 'field')
    change_list_template = 'change_list.html'

admin.site.register(Hito, HitoAdmin)
admin.site.register(AvanceFisicoFinanciero, AvanceFisicoFinancieroAdmin)
admin.site.register(UcMilestone, UcMilestoneAdmin)
admin.site.register(Sm2015Milestone, Sm2015MilestoneAdmin)
admin.site.register(Objective)
admin.site.register(GrantsFinances, GrantsFinancesAdmin)
admin.site.register(GrantsFinancesFields)
admin.site.register(Operation)
admin.site.register(LifeSave, LifeSaveAdmin)
admin.site.register(LifeSaveField)
