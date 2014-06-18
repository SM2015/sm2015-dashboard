# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OperationZones'
        db.create_table(u'tables_operationzones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tables.Operation'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('latlng', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'tables', ['OperationZones'])

        # Adding field 'Operation.number'
        db.add_column(u'tables_operation', 'number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Operation.executing_agency'
        db.add_column(u'tables_operation', 'executing_agency',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Operation.benefitted_population'
        db.add_column(u'tables_operation', 'benefitted_population',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'OperationZones'
        db.delete_table(u'tables_operationzones')

        # Deleting field 'Operation.number'
        db.delete_column(u'tables_operation', 'number')

        # Deleting field 'Operation.executing_agency'
        db.delete_column(u'tables_operation', 'executing_agency')

        # Deleting field 'Operation.benefitted_population'
        db.delete_column(u'tables_operation', 'benefitted_population')


    models = {
        u'core.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latlng': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'core.language': {
            'Meta': {'object_name': 'Language'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.audiencia': {
            'Meta': {'object_name': 'Audiencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.avancefisicofinanciero': {
            'Meta': {'object_name': 'AvanceFisicoFinanciero'},
            'alerta': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_financiero_actual': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_financiero_planificado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_fisico_planificado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_fisico_real': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avances_financieros_original_programado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avances_fisicos_original_programado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            'fecha_de_actualizacion': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'monto_comprometido': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'monto_desembolsado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'recomendacion': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'upcoming_policy_dialogue_events': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        u'tables.countrydetails': {
            'Meta': {'object_name': 'CountryDetails'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Country']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isech': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.CountryDetailsIsech']", 'null': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.CountryDetailsLevel']", 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True'}),
            'pago': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.CountryDetailsPago']", 'null': 'True'})
        },
        u'tables.countrydetailsisech': {
            'Meta': {'object_name': 'CountryDetailsIsech'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True'}),
            'numero': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'})
        },
        u'tables.countrydetailslevel': {
            'Meta': {'object_name': 'CountryDetailsLevel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True'})
        },
        u'tables.countrydetailspago': {
            'Meta': {'object_name': 'CountryDetailsPago'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'})
        },
        u'tables.countrydetailsvalues': {
            'Meta': {'object_name': 'CountryDetailsValues'},
            'country_detail': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.CountryDetails']"}),
            'denominador_reportado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numerador_reportado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'quarter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Quarter']"})
        },
        u'tables.countrydisbursement': {
            'Meta': {'object_name': 'CountryDisbursement'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'charger': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.CountryDisbursementCharger']", 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Country']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.Operation']", 'null': 'True'}),
            'quarter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Quarter']"}),
            'year': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'null': 'True'})
        },
        u'tables.countrydisbursementcharger': {
            'Meta': {'object_name': 'CountryDisbursementCharger'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'tables.countryoperation': {
            'Meta': {'object_name': 'CountryOperation'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Country']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'it_disbursements_actual': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'it_disbursements_planned': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'it_execution_actual': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'it_execution_planned': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'quarter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Quarter']"})
        },
        u'tables.countryoperationit': {
            'Meta': {'object_name': 'CountryOperationIT'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.Country']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'it': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'tables.estadoactual': {
            'Meta': {'object_name': 'EstadoActual'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.grantsfinances': {
            'Meta': {'object_name': 'GrantsFinances'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.GrantsFinancesFields']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quarter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Quarter']"}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'tables.grantsfinancesfields': {
            'Meta': {'object_name': 'GrantsFinancesFields'},
            'field_origin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.GrantsFinancesOrigin']", 'null': 'True'}),
            'field_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.GrantsFinancesType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        },
        u'tables.grantsfinancesorigin': {
            'Meta': {'object_name': 'GrantsFinancesOrigin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        },
        u'tables.grantsfinancestype': {
            'Meta': {'object_name': 'GrantsFinancesType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        },
        u'tables.hito': {
            'Meta': {'object_name': 'Hito'},
            'actividad_en_poa': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'acuerdo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'alerta_notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'audiencia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tables.Audiencia']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            'estado_actual': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.EstadoActual']", 'null': 'True', 'blank': 'True'}),
            'hito': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador_de_pago': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'quarter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Quarter']"}),
            'recomendacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tables.lifesave': {
            'Meta': {'object_name': 'LifeSave'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.LifeSaveField']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_saving': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'percentage': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'tables.lifesavefield': {
            'Meta': {'object_name': 'LifeSaveField'},
            'abbr': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True'})
        },
        u'tables.objective': {
            'Meta': {'object_name': 'Objective'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'objective': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.operation': {
            'Meta': {'object_name': 'Operation'},
            'benefitted_population': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            'executing_agency': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'finish_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'starting_date': ('django.db.models.fields.DateField', [], {})
        },
        u'tables.operationzones': {
            'Meta': {'object_name': 'OperationZones'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latlng': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Operation']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'tables.quarter': {
            'Meta': {'ordering': "['name']", 'object_name': 'Quarter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '7'})
        },
        u'tables.sm2015milestone': {
            'Meta': {'object_name': 'Sm2015Milestone'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'}),
            'hitos': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.Objective']", 'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.ucmilestone': {
            'Meta': {'object_name': 'UcMilestone'},
            'coordination_unit_milestone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'objective': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'quarter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Quarter']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tables']