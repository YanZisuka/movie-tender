from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.movie, name='movie'),
    path('<str:genre_group>/', views.genre, name='genre'),
    path('<str:keyword>/', views.keyword, name='keyword'),
]
