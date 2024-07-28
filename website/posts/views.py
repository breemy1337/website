from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import Posts

def index(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context=context)
