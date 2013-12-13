# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EstadoActual'
        db.create_table(u'tables_estadoactual', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'tables', ['EstadoActual'])

        # Adding model 'Audiencia'
        db.create_table(u'tables_audiencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'tables', ['Audiencia'])

        # Deleting field 'Hito.actividad_en_pod'
        db.delete_column(u'tables_hito', 'actividad_en_pod')

        # Adding field 'Hito.actividad_en_poa'
        db.add_column(u'tables_hito', 'actividad_en_poa',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Hito.recomendacion'
        db.alter_column(u'tables_hito', 'recomendacion', self.gf('django.db.models.fields.TextField')(default=None))

        # Renaming column for 'Hito.estado_actual' to match new field type.
        db.rename_column(u'tables_hito', 'estado_actual', 'estado_actual_id')
        # Changing field 'Hito.estado_actual'
        db.alter_column(u'tables_hito', 'estado_actual_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['tables.EstadoActual']))
        # Adding index on 'Hito', fields ['estado_actual']
        db.create_index(u'tables_hito', ['estado_actual_id'])


        # Changing field 'Hito.alerta_notas'
        db.alter_column(u'tables_hito', 'alerta_notas', self.gf('django.db.models.fields.TextField')(default=None))

        # Changing field 'Hito.acuerdo'
        db.alter_column(u'tables_hito', 'acuerdo', self.gf('django.db.models.fields.TextField')(default=None))

        # Changing field 'AvanceFisicoFinanciero.fecha_de_actualizacion'
        db.alter_column(u'tables_avancefisicofinanciero', 'fecha_de_actualizacion', self.gf('django.db.models.fields.DateField')(default=None))

    def backwards(self, orm):
        # Removing index on 'Hito', fields ['estado_actual']
        db.delete_index(u'tables_hito', ['estado_actual_id'])

        # Deleting model 'EstadoActual'
        db.delete_table(u'tables_estadoactual')

        # Deleting model 'Audiencia'
        db.delete_table(u'tables_audiencia')

        # Adding field 'Hito.actividad_en_pod'
        db.add_column(u'tables_hito', 'actividad_en_pod',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Hito.actividad_en_poa'
        db.delete_column(u'tables_hito', 'actividad_en_poa')


        # Changing field 'Hito.recomendacion'
        db.alter_column(u'tables_hito', 'recomendacion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Renaming column for 'Hito.estado_actual' to match new field type.
        db.rename_column(u'tables_hito', 'estado_actual_id', 'estado_actual')
        # Changing field 'Hito.estado_actual'
        db.alter_column(u'tables_hito', 'estado_actual', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Hito.alerta_notas'
        db.alter_column(u'tables_hito', 'alerta_notas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Hito.acuerdo'
        db.alter_column(u'tables_hito', 'acuerdo', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'AvanceFisicoFinanciero.fecha_de_actualizacion'
        db.alter_column(u'tables_avancefisicofinanciero', 'fecha_de_actualizacion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    models = {
        u'tables.audiencia': {
            'Meta': {'object_name': 'Audiencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.avancefisicofinanciero': {
            'Meta': {'object_name': 'AvanceFisicoFinanciero'},
            'alerta': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avance_financiero_actual': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avance_financiero_planificado': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avance_fisico_planificado': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avance_fisico_real': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avances_financieros_original_programado': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'avances_fisicos_original_programado': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Country']"}),
            'fecha_de_actualizacion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto_comprometido': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'monto_desembolsado': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'recomendacion': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'tables.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.estadoactual': {
            'Meta': {'object_name': 'EstadoActual'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tables.hito': {
            'Meta': {'object_name': 'Hito'},
            'actividad_en_poa': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'acuerdo': ('django.db.models.fields.TextField', [], {}),
            'alerta_notas': ('django.db.models.fields.TextField', [], {}),
            'audiencia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tables.Audiencia']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.Country']"}),
            'estado_actual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tables.EstadoActual']"}),
            'hito': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador_de_pago': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'recomendacion': ('django.db.models.fields.TextField', [], {}),
            'trimestre': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tables']
