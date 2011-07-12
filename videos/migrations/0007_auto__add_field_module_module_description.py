# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Module.module_description'
        db.add_column('videos_module', 'module_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Module.module_description'
        db.delete_column('videos_module', 'module_description')


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
            'module_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'module_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.stream': {
            'Meta': {'object_name': 'Stream'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tag_video_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['videos.Video']", 'through': "orm['videos.Video_Tag']", 'symmetrical': 'False'})
        },
        'videos.type': {
            'Meta': {'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Module']"}),
            'video_part': ('django.db.models.fields.IntegerField', [], {}),
            'video_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'video_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Type']"}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'videos.video_tag': {
            'Meta': {'object_name': 'Video_Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_tag_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Tag']"}),
            'video_tag_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Video']"})
        }
    }

    complete_apps = ['videos']
