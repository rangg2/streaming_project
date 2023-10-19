from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('tag/', views.tag, name='tag'),
    path('daily/', views.daily, name='daily'),
    path('recommend/', views.recommend, name='reco'),
    path('', views.main, name='main'),
    path('play/', views.play, name='play'),
    path('member/', views.member, name='member'),
    path("logout/", auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path("laftel/", views.laftel_view, name='laftel'),
    path('search/', views.search_anime, name='search_anime'),
    # path('anime/<int:anime_id>/', views.get_anime_info, name='get_anime_info'),
    path('get_anime_info/', views.get_anime_info, name='get_anime_info'),
]
