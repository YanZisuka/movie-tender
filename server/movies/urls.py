from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'),
    path('<int:movie_pk>/', views.MovieView.as_view(), name='movie'),
    path('<int:movie_pk>/accounts/<str:username>/', views.get_rating, name='get_rating'),
    path('staffs/', views.get_staff, name='get_staff'),
    path('genres/<str:genre_group>/', views.get_genre, name='get_genre'),
    path('keywords/<int:pick_num>/', views.get_movies_with_keywords, name='get_movies_with_keywords'),
]
