from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import PostForm

from .models import Post, Category
from .forms import CommentForm
# Create your views here.

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            # commits temporarily, and doesnt push to the database 
            comment.post = post
            comment.save()

        return redirect ('index')
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {
        'post': post,
        'form': form 
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    posts = category.posts.filter(status=Post.ACTIVE)


    return render(request, 'blog/category.html', {
        'category': category,
        'posts': posts
    })


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})

def my_posts(request):
    posts = Post.objects.filter(author=request.user).filter(status=Post.ACTIVE)
    # posts = request.user.posts.filter(status=Post.ACTIVE)
    return render(request, 'blog/myposts.html', {
        'posts': posts
        #this function would show users their active posts
    })


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            obj = form.instance
            alert = True
            
            return render(request, 'blog/new_post.html', {
                'form': form,
                'obj': obj,
                'alert': alert
    })
        return redirect ('index')
    else:
        form = PostForm()
        
    return render(request, 'blog/new_post.html', {
        'form': form
    })


def edit_post(request, slug):
    post = Post.objects.filter(author=request.user).filter(status=Post.ACTIVE).get(slug=slug)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my-posts')

    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/detail.html', {
        'form': form,
        'post': post,
        'title': 'edit post'
    })


def delete_post(request, slug):
    post = Post.objects.filter(author=request.user).filter(status=Post.ACTIVE).get(slug=slug)
    post.status = Post.DELETED
    post.save()
    messages.success(request, 'Your post has been successfully deleted')
    return redirect('my-posts')
