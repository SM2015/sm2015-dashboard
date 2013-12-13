from django.contrib import admin
from tables.models import Country, AvanceFisicoFinanciero, Hito

class HitoAdmin(admin.ModelAdmin):
    list_display = ('country', 'indicador_de_pago')

admin.site.register(Country)
admin.site.register(AvanceFisicoFinanciero)
admin.site.register(Hito, HitoAdmin)
