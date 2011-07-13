# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Video_Tag'
        db.delete_table('videos_video_tag')

        # Adding M2M table for field video_tag on 'Video'
        db.create_table('videos_video_video_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['videos.video'], null=False)),
            ('tag', models.ForeignKey(orm['videos.tag'], null=False))
        ))
        db.create_unique('videos_video_video_tag', ['video_id', 'tag_id'])


    def backwards(self, orm):
        
        # Adding model 'Video_Tag'
        db.create_table('videos_video_tag', (
            ('video_tag_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videos.Tag'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_tag_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videos.Video'])),
        ))
        db.send_create_signal('videos', ['Video_Tag'])

        # Removing M2M table for field video_tag on 'Video'
        db.delete_table('videos_video_video_tag')


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
            'module_prereqs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['videos.Module']", 'symmetrical': 'False'}),
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
            'tag_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'video_tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['videos.Tag']", 'symmetrical': 'False'}),
            'video_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'video_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['videos.Type']"}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['videos']
