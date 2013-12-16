# coding: utf-8
import inspect
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __unicode__(self):
        return self.name

class AvanceFisicoFinanciero(models.Model):
    country = models.ForeignKey(Country)

    fecha_de_actualizacion = models.DateField()
    avance_fisico_planificado = models.IntegerField(null=True, blank=True, default=None)
    avance_financiero_planificado = models.IntegerField(null=True, blank=True, default=None)
    avance_fisico_real = models.IntegerField(null=True, blank=True, default=None)
    avance_financiero_actual = models.IntegerField(null=True, blank=True, default=None)
    avances_fisicos_original_programado = models.IntegerField(null=True, blank=True, default=None)
    avances_financieros_original_programado = models.IntegerField(null=True, blank=True, default=None)
    monto_comprometido = models.IntegerField(null=True, blank=True, default=None)
    monto_desembolsado = models.IntegerField(null=True, blank=True, default=None)

    alerta = models.TextField(null=True, blank=True, default=None)
    recomendacion = models.TextField(null=True, blank=True, default=None)

    def __unicode__(self):
        return self.country.name

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

    indicador_de_pago = models.CharField(max_length=200, null=True, blank=True, default=None)
    hito = models.CharField(max_length=200, null=True, blank=True, default=None)
    trimestre = models.CharField(max_length=200, null=True, blank=True, default=None)
    audiencia = models.ManyToManyField(Audiencia)
    estado_actual = models.ForeignKey(EstadoActual)
    alerta_notas = models.TextField(null=True, blank=True)
    recomendacion = models.TextField(null=True, blank=True)
    acuerdo = models.TextField(null=True, blank=True)
    actividad_en_poa = models.CharField(max_length=200, null=True, blank=True, default=None)

    @classmethod
    def get_editable_fields(cls):
        return ('estado_actual', 'alerta_notas', 'recomendacion', 'acuerdo', 'actividad_en_poa')

    def __unicode__(self):
        return self.country.name

    @classmethod
    def get_attributes(cls):
        boring = dir(type('dummy', (object,), {}))
        return [item
                for item in inspect.getmembers(cls)
                if item[0] not in boring]

class UcMilestone(models.Model):
    objective = models.CharField(max_length=200, null=True, blank=True, default=None)
    coordination_unit_milestone = models.CharField(max_length=200, null=True, blank=True, default=None)
    quarter = models.CharField(max_length=200, null=True, blank=True, default=None)
    status = models.CharField(max_length=200, null=True, blank=True, default=None)
    status_2 = models.CharField(max_length=200, null=True, blank=True, default=None)

    @classmethod
    def get_editable_fields(cls):
        return ('objective', 'coordination_unit_milestone', 'quarter', 'status', 'status_2')