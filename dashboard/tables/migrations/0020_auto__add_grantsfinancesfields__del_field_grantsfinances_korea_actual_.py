# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GrantsFinancesFields'
        db.create_table(u'tables_grantsfinancesfields', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'tables', ['GrantsFinancesFields'])

        # Deleting field 'GrantsFinances.korea_actual'
        db.delete_column(u'tables_grantsfinances', 'korea_actual')

        # Deleting field 'GrantsFinances.contribution_real_gos'
        db.delete_column(u'tables_grantsfinances', 'contribution_real_gos')

        # Deleting field 'GrantsFinances.contribution_real_icss'
        db.delete_column(u'tables_grantsfinances', 'contribution_real_icss')

        # Deleting field 'GrantsFinances.contribution_accumulated_bmgf'
        db.delete_column(u'tables_grantsfinances', 'contribution_accumulated_bmgf')

        # Deleting field 'GrantsFinances.korean_tc_accumulated'
        db.delete_column(u'tables_grantsfinances', 'korean_tc_accumulated')

        # Deleting field 'GrantsFinances.contribution_accumulated_icss'
        db.delete_column(u'tables_grantsfinances', 'contribution_accumulated_icss')

        # Deleting field 'GrantsFinances.contribution_spanish_government'
        db.delete_column(u'tables_grantsfinances', 'contribution_spanish_government')

        # Deleting field 'GrantsFinances.contribution_donates'
        db.delete_column(u'tables_grantsfinances', 'contribution_donates')

        # Deleting field 'GrantsFinances.contribution_real_bmgf'
        db.delete_column(u'tables_grantsfinances', 'contribution_real_bmgf')

        # Adding field 'GrantsFinances.field'
        db.add_column(u'tables_grantsfinances', 'field',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tables.GrantsFinancesFields'], null=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.value'
        db.add_column(u'tables_grantsfinances', 'value',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'GrantsFinancesFields'
        db.delete_table(u'tables_grantsfinancesfields')

        # Adding field 'GrantsFinances.korea_actual'
        db.add_column(u'tables_grantsfinances', 'korea_actual',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.contribution_real_gos'
        db.add_column(u'tables_grantsfinances', 'contribution_real_gos',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.contribution_real_icss'
        db.add_column(u'tables_grantsfinances', 'contribution_real_icss',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.contribution_accumulated_bmgf'
        db.add_column(u'tables_grantsfinances', 'contribution_accumulated_bmgf',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.korean_tc_accumulated'
        db.add_column(u'tables_grantsfinances', 'korean_tc_accumulated',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.contribution_accumulated_icss'
        db.add_column(u'tables_grantsfinances', 'contribution_accumulated_icss',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.contribution_spanish_government'
        db.add_column(u'tables_grantsfinances', 'contribution_spanish_government',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.contribution_donates'
        db.add_column(u'tables_grantsfinances', 'contribution_donates',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GrantsFinances.contribution_real_bmgf'
        db.add_column(u'tables_grantsfinances', 'contribution_real_bmgf',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'GrantsFinances.field'
        db.delete_column(u'tables_grantsfinances', 'field_id')

        # Deleting field 'GrantsFinances.value'
        db.delete_column(u'tables_grantsfinances', 'value')


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
            'field': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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