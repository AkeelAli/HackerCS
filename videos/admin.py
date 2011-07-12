from videos.models import Type, Tag, Video_Tag, Association, Stream, Module, Video
from django.contrib import admin

########
#inlines
########
class VideoInline(admin.TabularInline):
	model=Video
	extra=4


#######
#admins
#######
class ModuleAdmin(admin.ModelAdmin):
	inlines=[VideoInline]
	search_fields=['module_title']
	list_display=('module_title','stream_titles')

class AssociationAdmin(admin.ModelAdmin):
	list_display=('association_stream_id', 'association_module_id', 'association_part')

class StreamAdmin(admin.ModelAdmin):
	list_display=('stream_title','module_titles')

class VideoAdmin(admin.ModelAdmin):
	list_display=('video_url','module_title_part')

admin.site.register(Type)
admin.site.register(Tag)
admin.site.register(Video_Tag)
admin.site.register(Association,AssociationAdmin)
admin.site.register(Stream,StreamAdmin)
admin.site.register(Module,ModuleAdmin)
admin.site.register(Video,VideoAdmin)
