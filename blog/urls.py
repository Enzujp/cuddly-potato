from django.urls import path

from . import views


urlpatterns = [
    path('new-post/', views.new_post, name="new-post"),
    path('<slug:slug>/', views.category, name="category_detail"),
    path('search/', views.search, name="search"),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name="post_detail"),
    path('my-posts', views.my_posts, name="my-posts"),
    path('new-post/edit-post/<slug:slug>/', views.edit_post, name="edit-post"),
    path('my-posts/delete-post/<slug:slug>/', views.delete_post, name="delete-post")
    
]