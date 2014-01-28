# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GrantsFinancesOrigin'
        db.create_table(u'tables_grantsfinancesorigin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'tables', ['GrantsFinancesOrigin'])

        # Adding model 'GrantsFinancesType'
        db.create_table(u'tables_grantsfinancestype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'tables', ['GrantsFinancesType'])

        # Deleting field 'GrantsFinancesFields.field'
        db.delete_column(u'tables_grantsfinancesfields', 'field')

        # Adding field 'GrantsFinancesFields.name'
        db.add_column(u'tables_grantsfinancesfields', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'GrantsFinancesFields.field_type'
        db.add_column(u'tables_grantsfinancesfields', 'field_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tables.GrantsFinancesType'], null=True),
                      keep_default=False)

        # Adding field 'GrantsFinancesFields.field_origin'
        db.add_column(u'tables_grantsfinancesfields', 'field_origin',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tables.GrantsFinancesOrigin'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'GrantsFinancesOrigin'
        db.delete_table(u'tables_grantsfinancesorigin')

        # Deleting model 'GrantsFinancesType'
        db.delete_table(u'tables_grantsfinancestype')

        # Adding field 'GrantsFinancesFields.field'
        db.add_column(u'tables_grantsfinancesfields', 'field',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=200),
                      keep_default=False)

        # Deleting field 'GrantsFinancesFields.name'
        db.delete_column(u'tables_grantsfinancesfields', 'name')

        # Deleting field 'GrantsFinancesFields.field_type'
        db.delete_column(u'tables_grantsfinancesfields', 'field_type_id')

        # Deleting field 'GrantsFinancesFields.field_origin'
        db.delete_column(u'tables_grantsfinancesfields', 'field_origin_id')


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
            'fecha_de_actualizacion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'monto_comprometido': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'monto_desembolsado': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'recomendacion': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
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
            'period': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'actividad_en_poa': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'acuerdo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'alerta_notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'audiencia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tables.Audiencia']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            'estado_actual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.EstadoActual']"}),
            'hito': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador_de_pago': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'recomendacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'trimestre': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.objective': {
            'Meta': {'object_name': 'Objective'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'objective': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.operation': {
            'Meta': {'object_name': 'Operation'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            'finish_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'starting_date': ('django.db.models.fields.DateField', [], {})
        },
        u'tables.sm2015milestone': {
            'Meta': {'object_name': 'Sm2015Milestone'},
            'hitos': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['tables.Objective']", 'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.ucmilestone': {
            'Meta': {'object_name': 'UcMilestone'},
            'coordination_unit_milestone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Language']"}),
            'objective': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'quarter': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tables']