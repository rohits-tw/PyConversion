import re
from django.shortcuts import redirect, render
from .models import Video
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Video_form
import os
from .tasks import VideoFunction
# Create your views here.

# Code of  convert mp4 to Gif ------------------->>     
def index(request):
    if request.method =='POST':
        form = Video_form(request.POST, request.FILES)
        if form.is_valid():
            form_file_data = form.cleaned_data['video']
            form_choice_data = form.cleaned_data['VIDEO_CHOICES']
            form_file_data = str(form_file_data)
            form_choice_data = str(form_choice_data)
            VideoFunction.delay(form_file_data,form_choice_data)
    else:
        form = Video_form()
    return render(request,"videocon.html",{'form':form})
