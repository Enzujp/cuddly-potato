from django.urls import path

from . import views


urlpatterns = [
    path('<slug:slug>/', views.detail, name="post_detail"),
    path('<slug:slug>/', views.category, name="category_detail")
]