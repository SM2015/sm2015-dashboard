# coding: utf-8
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

class AvanceFisicoFinanciero(models.Model):
    country = models.ForeignKey(Country)

    fecha_de_actualizacion = models.DateField()
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

class Audiencia(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class EstadoActual(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Hito(models.Model):
    country = models.ForeignKey(Country)

    indicador_de_pago = models.CharField(max_length=100, null=True, blank=True, default=None)
    hito = models.CharField(max_length=100, null=True, blank=True, default=None)
    trimestre = models.CharField(max_length=100, null=True, blank=True, default=None)
    audiencia = models.ManyToManyField(Audiencia)
    estado_actual = models.ForeignKey(EstadoActual)
    alerta_notas = models.TextField()
    recomendacion = models.TextField()
    acuerdo = models.TextField()
    actividad_en_poa = models.CharField(max_length=100, null=True, blank=True, default=None)

    def __unicode__(self):
        return self.country.name
