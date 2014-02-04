# coding: utf-8
import inspect
from openpyxl import load_workbook
from django.db import models
from core.models import Country, Language

class AvanceFisicoFinanciero(models.Model):
    country = models.ForeignKey(Country)
    language = models.ForeignKey(Language, default=1)

    fecha_de_actualizacion = models.DateField(null=True, default=None, blank=True)
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
    def upload_excel(cls, uploaded_file):
        wb = load_workbook(uploaded_file, data_only=True)
        sheets = [
            {'country': Country.objects.get(slug='belize'), 'sheet': wb.get_sheet_by_name('Belize') },
            {'country': Country.objects.get(slug='costa-rica'), 'sheet': wb.get_sheet_by_name('Costa Rica') },
            {'country': Country.objects.get(slug='el-salvador'), 'sheet': wb.get_sheet_by_name('El Salvador') },
            {'country': Country.objects.get(slug='guatemala'), 'sheet': wb.get_sheet_by_name('Guatemala') },
            {'country': Country.objects.get(slug='honduras'), 'sheet': wb.get_sheet_by_name('Honduras') },
            {'country': Country.objects.get(slug='mexico'), 'sheet': wb.get_sheet_by_name('Mexico') },
            {'country': Country.objects.get(slug='nicaragua'), 'sheet': wb.get_sheet_by_name('Nicaragua') },
            {'country': Country.objects.get(slug='panama'), 'sheet': wb.get_sheet_by_name('Panama') }
        ]
        
        language_es = Language.objects.get(acronym='es')

        for sheet in sheets:
            real_sheet = sheet.get('sheet')
            country = sheet.get('country')

            try:
                fecha_de_actualizacion = real_sheet.rows[0][2].value.date()
            except AttributeError:
                fecha_de_actualizacion = None

            try:
                alerta = real_sheet.rows[0][11].value
            except IndexError:
                alerta = ''

            try:
                recomendacion = real_sheet.rows[1][11].value
            except IndexError:
                recomendacion = ''

            cls.objects.create(
                language = language_es,
                country = country,
                fecha_de_actualizacion = fecha_de_actualizacion,
                avance_fisico_planificado = real_sheet.rows[0][4].value,
                avance_financiero_planificado = real_sheet.rows[0][6].value,
                avance_fisico_real = real_sheet.rows[1][4].value,
                avance_financiero_actual = real_sheet.rows[1][6].value,
                avances_fisicos_original_programado = real_sheet.rows[0][9].value,
                avances_financieros_original_programado = real_sheet.rows[1][9].value,
                monto_comprometido = real_sheet.rows[1][7].value,
                monto_desembolsado = real_sheet.rows[1][2].value,
                alerta = alerta,
                recomendacion = recomendacion 
            )

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

    indicador_de_pago = models.CharField(max_length=500, null=True, blank=True, default=None)
    hito = models.CharField(max_length=500, null=True, blank=True, default=None)
    trimestre = models.CharField(max_length=200, null=True, blank=True, default=None)
    audiencia = models.ManyToManyField(Audiencia)
    estado_actual = models.ForeignKey(EstadoActual, null=True, blank=True, default=None)
    alerta_notas = models.TextField(null=True, blank=True)
    recomendacion = models.TextField(null=True, blank=True)
    acuerdo = models.TextField(null=True, blank=True)
    actividad_en_poa = models.CharField(max_length=500, null=True, blank=True, default=None)

    @classmethod
    def upload_excel(cls, uploaded_file):
        wb = load_workbook(uploaded_file, data_only=True)
        sheets = [
            {'country': Country.objects.get(slug='belize'), 'sheet': wb.get_sheet_by_name('Belize') },
            {'country': Country.objects.get(slug='costa-rica'), 'sheet': wb.get_sheet_by_name('Costa Rica') },
            {'country': Country.objects.get(slug='el-salvador'), 'sheet': wb.get_sheet_by_name('El Salvador') },
            {'country': Country.objects.get(slug='guatemala'), 'sheet': wb.get_sheet_by_name('Guatemala') },
            {'country': Country.objects.get(slug='honduras'), 'sheet': wb.get_sheet_by_name('Honduras') },
            {'country': Country.objects.get(slug='mexico'), 'sheet': wb.get_sheet_by_name('Mexico') },
            {'country': Country.objects.get(slug='nicaragua'), 'sheet': wb.get_sheet_by_name('Nicaragua') },
            {'country': Country.objects.get(slug='panama'), 'sheet': wb.get_sheet_by_name('Panama') }
        ]
        
        language_es = Language.objects.get(acronym='es')

        for sheet in sheets:
            real_sheet = sheet.get('sheet')
            country = sheet.get('country')

            for row in real_sheet.rows:
                if row[0].row >= 6 and (row[1].value or row[2].value):
                    if row[4].value == 'Completed' or row[4].value == 'Cumplido':
                        estado_actual = EstadoActual.objects.get(name='Cumplido')
                    elif row[4].value == 'In Progress' or row[4].value == 'En proceso':
                        estado_actual = EstadoActual.objects.get(name='En proceso')
                    elif row[4].value == 'Delayed' or row[4].value == 'Retrasado':
                        estado_actual = EstadoActual.objects.get(name='Retrasado')
                    else:
                        estado_actual = None

                    hito = cls.objects.create(
                        language = language_es,
                        country = country,
                        indicador_de_pago = row[1].value,
                        hito = row[2].value,
                        trimestre = row[3].value,
                        estado_actual = estado_actual,
                        alerta_notas = row[6].value,
                        recomendacion = row[7].value,
                        acuerdo = row[8].value,
                        actividad_en_poa = row[9].value
                    )

                    if row[5].value:
                        text_audiencias = row[5].value.replace(' ', '').split(',')
                        for i in xrange(0, len(text_audiencias)):
                            audiencia_str = text_audiencias[i].replace('Country', 'Pais').replace('Donors', 'Donantes')
                            text_audiencias[i] = audiencia_str

                        audiencias = Audiencia.objects.filter(name__in=text_audiencias)
                        for audiencia in audiencias:
                            hito.audiencia.add(audiencia)
                        hito.save()

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
        wb = load_workbook(uploaded_file, data_only=True)
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

    hitos = models.CharField(max_length=500, null=True, blank=True, default=None)
    status = models.CharField(max_length=200, null=True, blank=True, default=None)
    observation = models.CharField(max_length=500, null=True, blank=True, default=None)

    @classmethod
    def upload_excel(cls, uploaded_file):
        wb = load_workbook(uploaded_file, data_only=True)
        sheet_en = wb.get_sheet_by_name('SM2015 Milestones_en-US')
        sheet_es = wb.get_sheet_by_name('SM2015 Milestones_es-ES')
        language_en = Language.objects.get(acronym='en')
        language_es = Language.objects.get(acronym='es')

        for row in sheet_en.rows:
            if not row[0].row == 1 and row[1].value:
                if row[0].value:
                    try:
                        objective = Objective.objects.get(objective=row[0].value)
                    except:
                        objective = Objective.objects.create(objective=row[0].value, language=language_en)

                cls.objects.create(
                    language = language_en,
                    objective = objective,
                    hitos = row[1].value,
                    status = row[2].value,
                    observation = row[3].value
                )

        for row in sheet_es.rows:
            if not row[0].row == 1 and row[1].value:
                if row[0].value:
                    try:
                        objective = Objective.objects.get(objective=row[0].value)
                    except:
                        objective = Objective.objects.create(objective=row[0].value, language=language_es)

                cls.objects.create(
                    language = language_es,
                    objective = objective,
                    hitos = row[1].value,
                    status = row[2].value,
                    observation = row[3].value
                )

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

    @classmethod
    def get_periods(cls):
        grants_periods = GrantsFinances.objects.values('period').order_by('period')
        periods = []

        for row in grants_periods:
            if not row['period'] in periods:
                periods.append(row['period'])
        return periods

    @classmethod
    def upload_excel(cls, uploaded_file):
        wb = load_workbook(uploaded_file, data_only=True)
        sheet = wb.get_sheet_by_name('D.1.1.')

        bmgf_origin = GrantsFinancesOrigin.objects.get(uuid="GRANTS_ORIGIN_BMFG")
        icss_origin = GrantsFinancesOrigin.objects.get(uuid="GRANTS_ORIGIN_ICSS")
        gos_origin = GrantsFinancesOrigin.objects.get(uuid="GRANTS_ORIGIN_GOS")
        korean_origin = GrantsFinancesOrigin.objects.get(uuid="GRANTS_ORIGIN_KOREAN")

        real_type =  GrantsFinancesType.objects.get(uuid="GRANTS_TYPE_REAL")
        expected_type =  GrantsFinancesType.objects.get(uuid="GRANTS_TYPE_EXPECTED")

        columns_index = {
                'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
                'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 
                'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 
                'W': 22, 'X': 23, 'Y': 24, 'Z': 25
        }
        map_rows = {
            5: {'field': GrantsFinancesFields.objects.get(field_origin=bmgf_origin, field_type=expected_type)},
            9: {'field': GrantsFinancesFields.objects.get(field_origin=icss_origin, field_type=expected_type)},       
            11: {'field': GrantsFinancesFields.objects.get(field_origin=gos_origin, field_type=expected_type)},       
            13: {'field': GrantsFinancesFields.objects.get(field_origin=korean_origin, field_type=expected_type)},       
            18: {'field': GrantsFinancesFields.objects.get(field_origin=bmgf_origin, field_type=real_type)},       
            22: {'field': GrantsFinancesFields.objects.get(field_origin=icss_origin, field_type=real_type)},       
            24: {'field': GrantsFinancesFields.objects.get(field_origin=gos_origin, field_type=real_type)},      
            26: {'field': GrantsFinancesFields.objects.get(field_origin=korean_origin, field_type=real_type)}       
        }
        
        period_row = sheet.rows[2]
        for row in sheet.rows:
            try:
                map_row = map_rows[row[0].row]
                for cell in row:
                    if cell.column not in ['A', 'B'] and cell.value:
                        cls.objects.create(
                            period = period_row[columns_index[cell.column]].value,
                            field = map_row['field'],
                            value = cell.value
                        ) 
            except KeyError:
                continue

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
