from django.db import models
from django.contrib.auth.models import User

class DashboardUser(models.Model):
    user = models.OneToOneField(User, verbose_name=u"Dashboard User")
    activation_key = models.CharField(max_length=100)
    forgot_password_token = models.CharField(max_length=100, null=True, blank=True, default=None)
    
    def __unicode__(self):
        return self.user.first_name

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u"Contry"
        verbose_name_plural = "Contries"

class avance_fisico_y_financiero(models.Model):
    country = models.ForeignKey(Country)

    fecha_de_actualizacion = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_fisico_planificado = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_financiero_planificado = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_fisico_real = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_financiero_actual = models.CharField(max_length=100, null=True, blank=True, default=None)
    avances_fisicos_original_programado = models.CharField(max_length=100, null=True, blank=True, default=None)
    avances_financieros_original_programado = models.CharField(max_length=100, null=True, blank=True, default=None)
    monto_comprometido = models.CharField(max_length=100, null=True, blank=True, default=None)
    monto_desembolsado = models.CharField(max_length=100, null=True, blank=True, default=None)
    alerta = models.CharField(max_length=100, null=True, blank=True, default=None)
    recomendacion = models.CharField(max_length=100, null=True, blank=True, default=None)

class hito(models.Model):
    country = models.ForeignKey(Country)

    indicador_de_pago = models.CharField(max_length=100, null=True, blank=True, default=None)
    hito = models.CharField(max_length=100, null=True, blank=True, default=None)
    trimestre = models.CharField(max_length=100, null=True, blank=True, default=None)
    audiencia = models.CharField(max_length=100, null=True, blank=True, default=None)
    estado_actual = models.CharField(max_length=100, null=True, blank=True, default=None)
    alerta_notas = models.CharField(max_length=100, null=True, blank=True, default=None)
    recomendacion = models.CharField(max_length=100, null=True, blank=True, default=None)
    acuerdo = models.CharField(max_length=100, null=True, blank=True, default=None)
    actividad_en_pod = models.CharField(max_length=100, null=True, blank=True, default=None)