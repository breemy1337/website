from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

def index(request):
    posts = Posts.objects.all()
    return HttpResponse(posts[1].location)
