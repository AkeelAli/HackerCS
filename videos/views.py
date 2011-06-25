from django.shortcuts import render_to_response
from videos.models import Video
from django.http import Http404

def index(request):
	latest_video_list=Video.objects.all()
	return render_to_response('videos/index.html',{'latest_video_list' : latest_video_list})

def detail(request,video_id):
	try:
		v=Video.objects.get(pk=video_id)
	except Video.DoesNotExist:
		raise Http404
	return render_to_response('videos/detail.html',{'video':v})
