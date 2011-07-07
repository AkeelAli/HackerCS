from django.db import models


class Stream(models.Model):
	title=models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.title

class Module(models.Model):
	title=models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.title

class Video(models.Model):
	module=models.ForeignKey(Module)
	url=models.CharField(max_length=200)

	def __unicode__(self):
		return self.url
