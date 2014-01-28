from django.contrib import admin
from tables.models import AvanceFisicoFinanciero, Hito, UcMilestone, \
        Sm2015Milestone, Objective, GrantsFinances, GrantsFinancesFields, Operation

class HitoAdmin(admin.ModelAdmin):
    list_display = ('country', 'indicador_de_pago')

class GrantsFinancesAdmin(admin.ModelAdmin):
    list_display = ('period', )

admin.site.register(Hito, HitoAdmin)
admin.site.register(AvanceFisicoFinanciero)
admin.site.register(UcMilestone)
admin.site.register(Sm2015Milestone)
admin.site.register(Objective)
admin.site.register(GrantsFinances, GrantsFinancesAdmin)
admin.site.register(GrantsFinancesFields)
admin.site.register(Operation)
