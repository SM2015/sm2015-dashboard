from django.contrib import admin
from tables.models import Country, AvanceFisicoFinanciero, Hito, UcMilestone, Sm2015Milestone, Objective

class HitoAdmin(admin.ModelAdmin):
    list_display = ('country', 'indicador_de_pago')

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Country, CountryAdmin)
admin.site.register(Hito, HitoAdmin)

admin.site.register(AvanceFisicoFinanciero)
admin.site.register(UcMilestone)
admin.site.register(Sm2015Milestone)
admin.site.register(Objective)