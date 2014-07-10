from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from core.models import DashboardUser


class DashboardUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(DashboardUserForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs.keys():
            instance = kwargs['instance']
            self.fields['first_name'].initial = instance.user.first_name
            self.fields['last_name'].initial = instance.user.last_name
            self.fields['username'].initial = instance.user.username
            self.fields['email'].initial = instance.user.email

    def save(self, *args, **kw):
        save_return = super(DashboardUserForm, self).save(*args, **kw)
        try:
            self.instance.user.username = self.cleaned_data.get('username')
            self.instance.user.first_name = self.cleaned_data.get('first_name')
            self.instance.user.last_name = self.cleaned_data.get('last_name')
            self.instance.user.email = self.cleaned_data.get('email')
            self.instance.user.save()
        except Exception:
            usuario = User.objects.create(
                username=self.cleaned_data.get('username'),
                first_name=self.cleaned_data.get('first_name'),
                last_name=self.cleaned_data.get('last_name'),
                email=self.cleaned_data.get('email')
            )
            self.instance.user = usuario

        return save_return

    class Meta:
        model = DashboardUser


class DashboardUserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'username', 'email', 'countries',
              'tables', 'have_database_access')
    form = DashboardUserForm

    def queryset(self, request):
        qs = super(DashboardUserAdmin, self).queryset(request)
        return qs.exclude(user__username='admin')


admin.site.register(DashboardUser, DashboardUserAdmin)
