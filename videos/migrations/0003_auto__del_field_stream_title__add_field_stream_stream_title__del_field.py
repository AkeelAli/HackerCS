# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Stream.title'
        db.delete_column('videos_stream', 'title')

        # Adding field 'Stream.stream_title'
        db.add_column('videos_stream', 'stream_title', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Deleting field 'Module.title'
        db.delete_column('videos_module', 'title')

        # Adding field 'Module.stream_id'
        db.add_column('videos_module', 'stream_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['videos.Stream']), keep_default=False)

        # Adding field 'Module.module_title'
        db.add_column('videos_module', 'module_title', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Deleting field 'Video.url'
        db.delete_column('videos_video', 'url')

        # Deleting field 'Video.module'
        db.delete_column('videos_video', 'module_id')

        # Adding field 'Video.module_id'
        db.add_column('videos_video', 'module_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['videos.Module']), keep_default=False)

        # Adding field 'Video.video_url'
        db.add_column('videos_video', 'video_url', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Adding field 'Video.video_title'
        db.add_column('videos_video', 'video_title', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Adding field 'Video.video_part'
        db.add_column('videos_video', 'video_part', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Stream.title'
        db.add_column('videos_stream', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Deleting field 'Stream.stream_title'
        db.delete_column('videos_stream', 'stream_title')

        # Adding field 'Module.title'
        db.add_column('videos_module', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Deleting field 'Module.stream_id'
        db.delete_column('videos_module', 'stream_id_id')

        # Deleting field 'Module.module_title'
        db.delete_column('videos_module', 'module_title')

        # Adding field 'Video.url'
        db.add_column('videos_video', 'url', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Adding field 'Video.module'
        db.add_column('videos_video', 'module', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['videos.Module']), keep_default=False)

        # Deleting field 'Video.module_id'
        db.delete_column('videos_video', 'module_id_id')

        # Deleting field 'Video.video_url'
        db.delete_column('videos_video', 'video_url')

        # Deleting field 'Video.video_title'
        db.delete_column('videos_video', 'video_title')

        # Deleting field 'Video.video_part'
        db.delete_column('videos_video', 'video_part')


    models = {
        'videos.module': {
            'Meta': {'object_name': 'Module'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stream_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Stream']"})
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
