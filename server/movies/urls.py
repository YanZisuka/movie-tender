from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.movie, name='movie'),
    path('<int:movie_pk>/accounts/<str:username>/', views.get_rating, name='get_rating'),
    path('staffs/', views.get_staff, name='get_staff'),
    path('genres/<str:genre_group>/', views.get_genre, name='get_genre'),
    path('keywords/<int:pick_num>/', views.get_movies_with_keyword, name='get_movies_with_keyword'),
]
