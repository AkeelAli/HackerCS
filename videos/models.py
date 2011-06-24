from django.db import models

class Video(models.Model):
	module=models.ForeignKey(Module)
	url=models.CharField(max_length=200)

class Module(models.Model):
	title=models.CharField(max_length=200)
