from videos.models import Module, Video
from django.contrib import admin

class VideoInline(admin.TabularInline):
	model=Video
	extra=4

class ModuleAdmin(admin.ModelAdmin):
	inlines=[VideoInline]
	search_fields=['title']

admin.site.register(Module,ModuleAdmin)
admin.site.register(Video)
