from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .models import Posts, Groups, User


def index(request):
    posts = Posts.objects.all().order_by('date')
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context=context)


def group_post(request, slug):
    group = get_object_or_404(Groups, slug=slug)
    posts = group.posts.select_related('groups')
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    context = {
            'post': post
        }
    return render(request, 'posts/post_detail.html', context=context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.select_related('groups')
    context = {
        'posts': posts,
        'author': author
    }
    return render(request, 'posts/profile.html', context=context)
