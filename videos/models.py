from django.db import models

class Type(models.Model):
	type_title=models.CharField(max_length=200)

	def __unicode__(self):
		return self.type_title

class Stream(models.Model):
	stream_title=models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.stream_title

	def module_titles(self):
		module_titles=[]
		for association in self.association_set.all():
			module=association.association_module_id.module_title
			module_titles.append(module)
		return '<br /> '.join(module_titles)
	module_titles.allow_tags=True

class Module(models.Model):
	module_associations=models.ManyToManyField(Stream, through='Association')
	module_title=models.CharField(max_length=200)
	module_description=models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.module_title

	def stream_titles(self):
		stream_titles=[]
		for association in self.association_set.all():
			stream=association.association_stream_id.stream_title
			stream_titles.append(stream)
		return ', '.join(stream_titles)

class Association(models.Model):
	association_stream_id=models.ForeignKey(Stream)
	association_module_id=models.ForeignKey(Module)
	association_part=models.IntegerField()

	def __unicode__(self):
		return "%s: %s (%d)" % (self.association_stream_id.stream_title, self.association_module_id.module_title, self.association_part)

class Video(models.Model):
	module_id=models.ForeignKey(Module)
	video_type=models.ForeignKey(Type)

	video_url=models.CharField(max_length=200)
	video_title=models.CharField(max_length=200, blank=True)
	video_part=models.IntegerField()

	def __unicode__(self):
		return "%s" % self.module_id.module_title + " ("+str(self.video_part)+")"

	def module_title_part(self):
		return "%s" % self.module_id.module_title + " ("+str(self.video_part)+")"

	def video_youtube_id(self):
		import re
		match=re.search("v=(.*)$",self.video_url)
		if match:
			return match.group(1)
		else:
			return ''
	
	def video_tags(self):
		tag_titles=[]
		for video_tag in self.video_tag_set.all():
			tag=video_tag.video_tag_tag.tag_title
			tag_titles.append(tag)
		return ', '.join(tag_titles)

class Tag(models.Model):
	tag_title=models.CharField(max_length=200)
	tag_video_tags=models.ManyToManyField(Video, through='Video_Tag')

	def __unicode__(self):
		return self.tag_title

class Video_Tag(models.Model):
	video_tag_video=models.ForeignKey(Video)
	video_tag_tag=models.ForeignKey(Tag)
	
