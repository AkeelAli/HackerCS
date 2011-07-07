# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Association'
        db.create_table('videos_association', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('association_stream_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videos.Stream'])),
            ('association_module_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videos.Module'])),
            ('association_part', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('videos', ['Association'])

        # Deleting field 'Module.stream_id'
        db.delete_column('videos_module', 'stream_id_id')


    def backwards(self, orm):
        
        # Deleting model 'Association'
        db.delete_table('videos_association')

        # Adding field 'Module.stream_id'
        db.add_column('videos_module', 'stream_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['videos.Stream']), keep_default=False)


    models = {
        'videos.association': {
            'Meta': {'object_name': 'Association'},
            'association_module_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Module']"}),
            'association_part': ('django.db.models.fields.IntegerField', [], {}),
            'association_stream_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Stream']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'videos.module': {
            'Meta': {'object_name': 'Module'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_associations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['videos.Stream']", 'through': "orm['videos.Association']", 'symmetrical': 'False'}),
            'module_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.stream': {
            'Meta': {'object_name': 'Stream'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Module']"}),
            'video_part': ('django.db.models.fields.IntegerField', [], {}),
            'video_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['videos']
