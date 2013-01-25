# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Users'
        db.create_table(u'meta_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('paycheck', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('date_joined', self.gf('django.db.models.fields.DateField')(max_length=100)),
        ))
        db.send_create_signal(u'meta', ['Users'])

        # Adding model 'Rooms'
        db.create_table(u'meta_rooms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('spots', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
        ))
        db.send_create_signal(u'meta', ['Rooms'])


    def backwards(self, orm):
        # Deleting model 'Users'
        db.delete_table(u'meta_users')

        # Deleting model 'Rooms'
        db.delete_table(u'meta_rooms')


    models = {
        u'meta.rooms': {
            'Meta': {'object_name': 'Rooms'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': '100'})
        },
        u'meta.users': {
            'Meta': {'object_name': 'Users'},
            'date_joined': ('django.db.models.fields.DateField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['meta']