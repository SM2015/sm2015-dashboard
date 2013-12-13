# coding: utf-8
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

class AvanceFisicoFinanciero(models.Model):
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

class Hito(models.Model):
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

    def __unicode__(self):
        return self.country.name

class HitoAudiencia(models.Model):
    name = models.Charfield()

    def __unicode__(self):
        return self.name
