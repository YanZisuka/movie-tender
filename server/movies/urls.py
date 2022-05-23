from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.movie, name='movie'),
    path('staffs/', views.get_staff, name='get_staff'),
    path('genres/<str:genre_group>/', views.get_genre, name='get_genre'),
    path('keywords/<int:keyword_pk>/', views.get_keyword, name='get_keyword'),
]
