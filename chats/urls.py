from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('index/', views.index, name='home'),
    path('<str:username>/', views.chatPage, name='chat'),
]
