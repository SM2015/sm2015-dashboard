# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.datetime'
        db.delete_column(u'sm2015_calendar_event', 'datetime')

        # Adding field 'Event.start'
        db.add_column(u'sm2015_calendar_event', 'start',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Event.end'
        db.add_column(u'sm2015_calendar_event', 'end',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True),
                      keep_default=False)

        # Adding field 'Event.all_day'
        db.add_column(u'sm2015_calendar_event', 'all_day',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Event.datetime'
        db.add_column(u'sm2015_calendar_event', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Event.start'
        db.delete_column(u'sm2015_calendar_event', 'start')

        # Deleting field 'Event.end'
        db.delete_column(u'sm2015_calendar_event', 'end')

        # Deleting field 'Event.all_day'
        db.delete_column(u'sm2015_calendar_event', 'all_day')


    models = {
        u'sm2015_calendar.event': {
            'Meta': {'object_name': 'Event'},
            'all_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['sm2015_calendar']