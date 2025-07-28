from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name='home'),
    path('home', views.home, name='home'),
     path("sign-up/", views.sign_up, name='sign_up'),
    path("login/", views.user_login, name='login'),
    path('create-post', views.create_post, name='create_post'), 
    
]