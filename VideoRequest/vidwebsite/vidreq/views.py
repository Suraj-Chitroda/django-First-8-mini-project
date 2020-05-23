from django.shortcuts import render, redirect
from . models import Video
from . forms import VideoForms
# Create your views here.

def index(request):
    
    vid = Video.objects.order_by('-date_added')
    context = {'videos':vid}
    return render(request, 'vidreq/index.html', context)

def vidrequest(request):
    if(request.method == 'POST'):
        form = VideoForms(request.POST)
        
        if form.is_valid():
            new_req = Video(video_title=request.POST['vidname'], video_desc=request.POST['viddesc'])
            new_req.save()
            return redirect('index')
    else:
        form = VideoForms()

    context = {'frm': form}
    return render(request, 'vidreq/vidform.html', context)

