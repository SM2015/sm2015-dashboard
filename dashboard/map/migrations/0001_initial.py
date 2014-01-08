# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Map'
        db.create_table(u'map_map', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Country'])),
            ('coord', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('more_info', self.gf('django.db.models.fields.TextField')()),
            ('goal', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'map', ['Map'])


    def backwards(self, orm):
        # Deleting model 'Map'
        db.delete_table(u'map_map')


    models = {
        u'core.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'map.map': {
            'Meta': {'object_name': 'Map'},
            'coord': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Country']"}),
            'goal': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'more_info': ('django.db.models.fields.TextField', [], {}),
            'short_description': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['map']