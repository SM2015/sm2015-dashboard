# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'tables_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'tables', ['Country'])

        # Adding model 'AvanceFisicoFinanciero'
        db.create_table(u'tables_avancefisicofinanciero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tables.Country'])),
            ('fecha_de_actualizacion', self.gf('django.db.models.fields.DateField')()),
            ('avance_fisico_planificado', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('avance_financiero_planificado', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('avance_fisico_real', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('avance_financiero_actual', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('avances_fisicos_original_programado', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('avances_financieros_original_programado', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('monto_comprometido', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('monto_desembolsado', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('alerta', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('recomendacion', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'tables', ['AvanceFisicoFinanciero'])

        # Adding model 'Audiencia'
        db.create_table(u'tables_audiencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'tables', ['Audiencia'])

        # Adding model 'EstadoActual'
        db.create_table(u'tables_estadoactual', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'tables', ['EstadoActual'])

        # Adding model 'Hito'
        db.create_table(u'tables_hito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tables.Country'])),
            ('indicador_de_pago', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('hito', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('trimestre', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('estado_actual', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tables.EstadoActual'])),
            ('alerta_notas', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('recomendacion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('acuerdo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actividad_en_poa', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'tables', ['Hito'])

        # Adding M2M table for field audiencia on 'Hito'
        m2m_table_name = db.shorten_name(u'tables_hito_audiencia')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hito', models.ForeignKey(orm[u'tables.hito'], null=False)),
            ('audiencia', models.ForeignKey(orm[u'tables.audiencia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hito_id', 'audiencia_id'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'tables_country')

        # Deleting model 'AvanceFisicoFinanciero'
        db.delete_table(u'tables_avancefisicofinanciero')

        # Deleting model 'Audiencia'
        db.delete_table(u'tables_audiencia')

        # Deleting model 'EstadoActual'
        db.delete_table(u'tables_estadoactual')

        # Deleting model 'Hito'
        db.delete_table(u'tables_hito')

        # Removing M2M table for field audiencia on 'Hito'
        db.delete_table(db.shorten_name(u'tables_hito_audiencia'))


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        }
    }

    complete_apps = ['tables']
