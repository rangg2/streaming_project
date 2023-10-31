from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from main.views import list_kinesis_streams
from django.urls import path
from .views import AnimeInfoAPIView, AnimeView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('tag/', views.tag, name='tag'),
    path('daily/', views.daily, name='daily'),
    path('recommend/', views.recommend, name='reco'),
    # path('', views.main, name='main'),
    path('', views.Anime_list, name='main'),
    path('play/', views.play, name='play'),
    path('member/', views.member, name='member'),
    path("logout/", auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path("laftel/", views.laftel_view, name='laftel'),
    path('search/', views.search_anime, name='search_anime'),
    # path('anime/<int:anime_id>/', views.get_anime_info, name='get_anime_info'),
    path('get_anime_info/', views.get_anime_info, name='get_anime_info'),
    path('api/anime/', AnimeInfoAPIView.as_view(), name='anime_api'),
    path('list_streams/', list_kinesis_streams, name='list_streams'),
    path('anime-list/', AnimeView.as_view(), name='anime_list')
]
