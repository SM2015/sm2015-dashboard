# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        belize = orm.Country.objects.get(id=1)
        costa_rica = orm.Country.objects.get(id=2)
        el_salvador = orm.Country.objects.get(id=3)
        guatemala = orm.Country.objects.get(id=4)
        honduras = orm.Country.objects.get(id=5)
        mexico = orm.Country.objects.get(id=6)
        nicaragua = orm.Country.objects.get(id=7)
        panama = orm.Country.objects.get(id=8)

        belize.latlng = '17.210867,-88.625366'
        costa_rica.latlng = '9.748917,-83.753428'
        el_salvador.latlng = '13.794185,-88.896530'
        guatemala.latlng = '15.529582,-90.230759'
        honduras.latlng = '15.199999,-86.241905'
        mexico.latlng = '23.634501,-102.552784'
        nicaragua.latlng = '12.865416,-85.207229'
        panama.latlng = '8.537981,-80.782127'

        belize.save()
        costa_rica.save()
        el_salvador.save()
        guatemala.save()
        honduras.save()
        mexico.save()
        nicaragua.save()
        panama.save()

    def backwards(self, orm):
        belize = orm.Country.objects.get(id=1)
        costa_rica = orm.Country.objects.get(id=2)
        el_salvador = orm.Country.objects.get(id=3)
        guatemala = orm.Country.objects.get(id=4)
        honduras = orm.Country.objects.get(id=5)
        mexico = orm.Country.objects.get(id=6)
        nicaragua = orm.Country.objects.get(id=7)
        panama = orm.Country.objects.get(id=8)

        belize.latlng = ''
        costa_rica.latlng = ''
        el_salvador.latlng = ''
        guatemala.latlng = ''
        honduras.latlng = ''
        mexico.latlng = ''
        nicaragua.latlng = ''
        panama.latlng = ''

        belize.save()
        costa_rica.save()
        el_salvador.save()
        guatemala.save()
        honduras.save()
        mexico.save()
        nicaragua.save()
        panama.save()

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latlng': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'core.dashboarduser': {
            'Meta': {'object_name': 'DashboardUser'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Country']", 'symmetrical': 'False'}),
            'forgot_password_token': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['core']
    symmetrical = True
