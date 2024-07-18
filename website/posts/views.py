from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

def index(request):
    posts = Posts.objects.all()
    return HttpResponse(posts[1].location)

def post_id(request, id):
    posts = Posts.objects.all()
    if id > len(posts):
        return HttpResponse('пшел нах дурачек ахуевший червячок')
    return HttpResponse(posts[id].text)
