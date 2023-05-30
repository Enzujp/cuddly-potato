from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login

from blog.models import Post, Category
from blog.forms import SignupForm, PostForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('index')
    
    else:
        form = SignupForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })

def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


def my_posts(request):
    posts = request.author.posts.filter(status=Post.ACTIVE)
    return render(request, 'userprofile/myposts.html', {
        'posts': posts
        #this function would show users their active posts
    })


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('my-posts')
    else:
        form = PostForm()
        
    return render(request, 'userprofile/new_post.html', {
        'form': form
    })


def edit_post(request, slug):
    post = Post.objects.filter(status=Post.ACTIVE).get(slug=slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()

    else:
        form = PostForm(instance=post)
    
    return render(request, 'userprofile/details.html', {
        'form': form,
        'post': post
    })


def delete_post(request, slug):
    post = Post.objects.filter(status=Post.ACTIVE).get(slug=slug)
    post.status = Post.DELETED
    post.save()
    return redirect('index')
