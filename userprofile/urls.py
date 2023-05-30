from django.urls import path
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='userprofile/logout.html'), name="logout"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('new-post/', views.new_post, name="new-post"),
    path('my-posts', views.my_posts, name="my-posts"),
    path('my-posts/edit-post/<slug:slug>/', views.edit_post, name="edit_post"),
    path('my-posts/delete-post/<slug:slug>/', views.delete_post, name="delete-post")
]