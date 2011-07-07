from django.db import models


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
	video_url=models.CharField(max_length=200)
	video_title=models.CharField(max_length=200, blank=True)
	video_part=models.IntegerField()

	def __unicode__(self):
		return self.video_url

	def module_title_part(self):
		return "%s" % self.module_id.module_title + " ("+str(self.video_part)+")"
