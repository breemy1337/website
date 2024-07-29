from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import Posts, Groups

def index(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context=context)

def group_post(request, slug):
    group = get_object_or_404(Groups, slug=slug)
    posts = group.posts.select_related('group')
    context = {
        'group' : group,
        'posts' : posts
    }
