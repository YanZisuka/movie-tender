from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.movie, name='movie'),
    path('genre/<str:genre_group>/', views.genre, name='genre'),
    path('keyword/<int:keyword_pk>/', views.keyword, name='keyword'),
]
