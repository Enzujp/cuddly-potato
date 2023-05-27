from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/index.html', {
        'posts': posts
    })

def about (request):
    return render(request, 'core/about.html')

