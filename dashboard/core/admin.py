from django.contrib import admin
from core.models import DashboardUser

class DashboardUserAdmin(admin.ModelAdmin):
    fields = ('user', 'countries',)
    readonly_fields = ('user',)

admin.site.register(DashboardUser, DashboardUserAdmin)
