# coding: utf-8
from django.contrib import admin
from tables.models import AvanceFisicoFinanciero, Hito, UcMilestone, \
    Sm2015Milestone, Objective, GrantsFinances, GrantsFinancesFields, \
    Operation, LifeSave, LifeSaveField, CountryDisbursement, \
    CountryDisbursementCharger, CountryOperation, CountryOperationIT, \
    CountryDetails, OperationZones, OperationTotalInvestment, OperationInfos, \
    CountryRiskIdentification, CountryMainRisks


class HitoAdmin(admin.ModelAdmin):
    list_display = ('country', 'indicador_de_pago', 'language')
    list_filter = ('country', 'indicador_de_pago', 'language')
    change_list_template = 'change_list_sheet_asking.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = {}
        extra_context['ask_sheet'] = True
        return super(HitoAdmin, self).changelist_view(request,
                                                      extra_context)


class GrantsFinancesAdmin(admin.ModelAdmin):
    list_display = ('quarter', 'field')
    list_filter = ('quarter', 'field')
    change_list_template = 'change_list.html'


class UcMilestoneAdmin(admin.ModelAdmin):
    list_display = ('coordination_unit_milestone', 'quarter', 'language')
    list_filter = ('coordination_unit_milestone', 'quarter', 'language')
    change_list_template = 'change_list_sheet_asking.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = {}
        extra_context['ask_sheet'] = True
        return super(UcMilestoneAdmin, self).changelist_view(request,
                                                             extra_context)


class AvanceFisicoFinancieroAdmin(admin.ModelAdmin):
    list_display = ('country', 'language')
    list_filter = ('country', 'language')
    change_list_template = 'change_list_sheet_asking.html'


class Sm2015MilestoneAdmin(admin.ModelAdmin):
    change_list_template = 'change_list_sheet_asking.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = {}
        extra_context['ask_sheet'] = True
        return super(Sm2015MilestoneAdmin, self).changelist_view(request,
                                                                 extra_context)


class LifeSaveAdmin(admin.ModelAdmin):
    list_display = ('country', 'field')
    list_filter = ('country', 'field')
    change_list_template = 'change_list.html'


class CountryDisbursementAdmin(admin.ModelAdmin):
    list_display = ('country', 'charger', 'quarter')
    list_filter = ('country', 'charger', 'quarter')
    change_list_template = 'change_list.html'


class CountryOperationAdmin(admin.ModelAdmin):
    list_display = ('country', 'quarter')
    list_filter = ('country', 'quarter')
    change_list_template = 'change_list.html'


class CountryDetailsAdmin(admin.ModelAdmin):
    list_display = ('country', 'pago', 'level', 'location')
    list_filter = ('country', 'pago', 'level', 'location')
    change_list_template = 'change_list_sheet_asking.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = {}
        extra_context['ask_country'] = True
        return super(CountryDetailsAdmin, self).changelist_view(request,
                                                                extra_context)


class OperationZonesAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'operation')

    def country(self, obj):
        return obj.operation.country.name


class OperationInfosAdmin(admin.ModelAdmin):
    list_display = ('operation', 'language')
    list_filter = ('operation', 'language')


class CountryRiskIdentificationAdmin(admin.ModelAdmin):
    list_display = ('country', 'field', 'level', 'type')
    list_filter = ('country', 'field', 'level', 'type')
    change_list_template = 'change_list.html'


class CountryMainRisksAdmin(admin.ModelAdmin):
    list_display = ('country', 'level', 'type')
    list_filter = ('country', 'level', 'type')
    change_list_template = 'change_list.html'


admin.site.register(Hito, HitoAdmin)
admin.site.register(AvanceFisicoFinanciero, AvanceFisicoFinancieroAdmin)
admin.site.register(UcMilestone, UcMilestoneAdmin)
admin.site.register(Sm2015Milestone, Sm2015MilestoneAdmin)
admin.site.register(Objective)
admin.site.register(GrantsFinances, GrantsFinancesAdmin)
admin.site.register(GrantsFinancesFields)
admin.site.register(Operation)
admin.site.register(OperationZones, OperationZonesAdmin)
admin.site.register(OperationInfos, OperationInfosAdmin)
admin.site.register(OperationTotalInvestment)
admin.site.register(LifeSave, LifeSaveAdmin)
admin.site.register(LifeSaveField)
admin.site.register(CountryDisbursement, CountryDisbursementAdmin)
admin.site.register(CountryDisbursementCharger)
admin.site.register(CountryOperation, CountryOperationAdmin)
admin.site.register(CountryOperationIT)
admin.site.register(CountryDetails, CountryDetailsAdmin)
admin.site.register(CountryRiskIdentification, CountryRiskIdentificationAdmin)
admin.site.register(CountryMainRisks, CountryMainRisksAdmin)
