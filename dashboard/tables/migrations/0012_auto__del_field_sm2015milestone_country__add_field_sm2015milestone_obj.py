# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sm2015Milestone.country'
        db.delete_column(u'tables_sm2015milestone', 'country_id')

        # Adding field 'Sm2015Milestone.objective'
        db.add_column(u'tables_sm2015milestone', 'objective',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['tables.Objective']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Sm2015Milestone.country'
        db.add_column(u'tables_sm2015milestone', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['tables.Objective']),
                      keep_default=False)

        # Deleting field 'Sm2015Milestone.objective'
        db.delete_column(u'tables_sm2015milestone', 'objective_id')


    models = {
        u'tables.audiencia': {
            'Meta': {'object_name': 'Audiencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.avancefisicofinanciero': {
            'Meta': {'object_name': 'AvanceFisicoFinanciero'},
            'alerta': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_financiero_actual': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_financiero_planificado': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_fisico_planificado': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avance_fisico_real': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avances_financieros_original_programado': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'avances_fisicos_original_programado': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Country']"}),
            'fecha_de_actualizacion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto_comprometido': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'monto_desembolsado': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'recomendacion': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'tables.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'tables.estadoactual': {
            'Meta': {'object_name': 'EstadoActual'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.hito': {
            'Meta': {'object_name': 'Hito'},
            'actividad_en_poa': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'acuerdo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'alerta_notas': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'audiencia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tables.Audiencia']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Country']"}),
            'estado_actual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.EstadoActual']"}),
            'hito': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador_de_pago': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'recomendacion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'trimestre': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.objective': {
            'Meta': {'object_name': 'Objective'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.sm2015milestone': {
            'Meta': {'object_name': 'Sm2015Milestone'},
            'hitos': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Objective']"}),
            'observation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tables.ucmilestone': {
            'Meta': {'object_name': 'UcMilestone'},
            'coordination_unit_milestone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objective': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'observation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'quarter': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tables']