from django.urls import path
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('profile', views.profile, name="profile"),
    path('edit-profile', views.edit_profile, name="edit-profile")
]