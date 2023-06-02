from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate
from  django.contrib.auth.forms import AuthenticationForm

from blog.models import Post, Category
from userprofile.models import Profile
from blog.forms import SignupForm, PostForm, UserProfileForm
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


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
                
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'invalid username or password')
    else:
        form = AuthenticationForm()
    
    return render(request, 'userprofile/login.html', {
        'form': form
    })


def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out, we hope to see you back sometime soon!')
    return redirect('index')

@login_required
def myaccount(request):
    return render(request, 'userprofile/accounts.html')

@login_required
def profile(request):
    return render(request, 'userprofile/profile.html')

@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

    return render(request, 'userprofile/edit_profile.html', {
        'profile': profile
    })



