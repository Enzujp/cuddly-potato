from django.shortcuts import render

from blog.models import Post


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', {
        'posts': posts
    })

def about (request):
    return render(request, 'core/about.html')

