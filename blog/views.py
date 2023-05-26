from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import CommentForm
# Create your views here.

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            # commits temporarily, and doesnt push to the database 
            comment.post = post
            comment.save()

        return redirect ('detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'form': form 
    })

