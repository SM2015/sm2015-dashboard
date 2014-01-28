# coding: utf-8
import inspect
from openpyxl import load_workbook
from django.db import models
from core.models import Country, Language

class AvanceFisicoFinanciero(models.Model):
    country = models.ForeignKey(Country)
    language = models.ForeignKey(Language, default=1)

    fecha_de_actualizacion = models.DateField()
    avance_fisico_planificado = models.FloatField(null=True, blank=True, default=None)
    avance_financiero_planificado = models.FloatField(null=True, blank=True, default=None)
    avance_fisico_real = models.FloatField(null=True, blank=True, default=None)
    avance_financiero_actual = models.FloatField(null=True, blank=True, default=None)
    avances_fisicos_original_programado = models.FloatField(null=True, blank=True, default=None)
    avances_financieros_original_programado = models.FloatField(null=True, blank=True, default=None)
    monto_comprometido = models.FloatField(null=True, blank=True, default=None)
    monto_desembolsado = models.FloatField(null=True, blank=True, default=None)

    alerta = models.TextField(null=True, blank=True, default=None)
    recomendacion = models.TextField(null=True, blank=True, default=None)

    @classmethod
    def get_editable_fields(cls):
        return ('fecha_de_actualizacion', 'avance_fisico_planificado', 'avance_financiero_planificado',
        'avance_fisico_real','avance_financiero_actual','avances_fisicos_original_programado',
        'avances_financieros_original_programado','monto_desembolsado','monto_comprometido',
        'alerta','recomendacion')

    def __unicode__(self):
        return self.country.name

class Audiencia(models.Model):
    language = models.ForeignKey(Language, default=1)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class EstadoActual(models.Model):
    language = models.ForeignKey(Language, default=1)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Hito(models.Model):
    country = models.ForeignKey(Country)
    language = models.ForeignKey(Language, default=1)

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

class UcMilestone(models.Model):
    language = models.ForeignKey(Language, default=1)
    objective = models.CharField(max_length=300, null=True, blank=True, default=None)
    coordination_unit_milestone = models.CharField(max_length=500, null=True, blank=True, default=None)
    quarter = models.CharField(max_length=200, null=True, blank=True, default=None)
    status = models.CharField(max_length=200, null=True, blank=True, default=None)
    observation = models.CharField(max_length=500, null=True, blank=True, default=None)

    @classmethod
    def upload_excel(cls, uploaded_file):
        wb = load_workbook(uploaded_file)
        sheet_en = wb.get_sheet_by_name('UC Milestones_en-US')
        sheet_es = wb.get_sheet_by_name('UC Milestones_es-ES')
        language_en = Language.objects.get(acronym='en')
        language_es = Language.objects.get(acronym='es')

        for row in sheet_en.rows:
            if not row[0].row == 1 and row[0].value:
                cls.objects.create(
                    language = language_en,
                    objective = row[0].value,
                    coordination_unit_milestone = row[1].value,
                    quarter = row[2].value,
                    status = row[3].value,
                    observation = row[4].value
                )

        for row in sheet_es.rows:
            if not row[0].row == 1 and row[0].value:
                cls.objects.create(
                    language = language_es,
                    objective = row[0].value,
                    coordination_unit_milestone = row[1].value,
                    quarter = row[2].value,
                    status = row[3].value,
                    observation = row[4].value
                )

    @classmethod
    def get_editable_fields(cls):
        return ('objective', 'coordination_unit_milestone', 'quarter', 'status', 'observation')

    def __unicode__(self):
        return self.coordination_unit_milestone

class Objective(models.Model):
    language = models.ForeignKey(Language, default=1)
    objective = models.CharField(max_length=200, null=True, blank=True, default=None)
    
    def __unicode__(self):
        return self.objective

class Sm2015Milestone(models.Model):
    objective = models.ForeignKey(Objective, null=True, blank=True, default=None)
    language = models.ForeignKey(Language, default=1)

    hitos = models.CharField(max_length=200, null=True, blank=True, default=None)
    status = models.CharField(max_length=200, null=True, blank=True, default=None)
    observation = models.CharField(max_length=200, null=True, blank=True, default=None)

    @classmethod
    def get_editable_fields(cls):
        return ('hitos', 'status', 'observation')

    def __unicode__(self):
        return self.hitos

class GrantsFinancesType(models.Model):
    name = models.CharField(max_length=200, default='')
    uuid = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return self.name

class GrantsFinancesOrigin(models.Model):
    name = models.CharField(max_length=200, default='')
    uuid = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return self.name

class GrantsFinancesFields(models.Model):
    name = models.CharField(max_length=200, default='')
    field_type = models.ForeignKey(GrantsFinancesType, null=True)
    field_origin = models.ForeignKey(GrantsFinancesOrigin, null=True)

    @classmethod
    def get_editable_fields(cls):
        return ('name', 'field_origin', 'field_type')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Grants & Finances Fields'
        verbose_name = u'Grants & Finances Fields'

class GrantsFinances(models.Model):
    period = models.CharField(max_length=200, default=None, null=True, blank=True)
    field = models.ForeignKey(GrantsFinancesFields, null=True)
    value = models.FloatField(default=0)

    @classmethod
    def get_editable_fields(cls):
        return ('value',)

    def __unicode__(self):
        return self.field.name

    class Meta:
        verbose_name_plural = u'Grants & Finances'
        verbose_name = u'Grants & Finances'

class Operation(models.Model):
    country = models.ForeignKey(Country)

    starting_date = models.DateField()
    finish_date = models.DateField()

    def __unicode__(self):
        return self.country.name
