# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Stream'
        db.create_table('videos_stream', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('videos', ['Stream'])

        # Adding field 'Module.stream'
        db.add_column('videos_module', 'stream', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['videos.Stream']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Stream'
        db.delete_table('videos_stream')

        # Deleting field 'Module.stream'
        db.delete_column('videos_module', 'stream_id')


    models = {
        'videos.module': {
            'Meta': {'object_name': 'Module'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Stream']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.stream': {
            'Meta': {'object_name': 'Stream'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Module']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['videos']
