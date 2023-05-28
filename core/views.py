from django.shortcuts import render
from  django.http import HttpResponse

from blog.models import Post


def index(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/index.html', {
        'posts': posts
    })

def about (request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")