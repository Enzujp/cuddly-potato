from django.urls import path
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('profile', views.profile, name="profile"),
    path('edit-profile', views.edit_profile, name="edit-profile"),
    path('new-post/', views.new_post, name="new-post"),
    path('my-posts', views.my_posts, name="my-posts"),
    path('my-posts/edit-post/<slug:slug>/', views.edit_post, name="edit_post"),
    path('my-posts/delete-post/<slug:slug>/', views.delete_post, name="delete-post")
]