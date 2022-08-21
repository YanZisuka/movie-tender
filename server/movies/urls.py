from django.urls import path
from movies import views


app_name = "movies"

urlpatterns = [
    path(
        "",
        views.MovieViewSet.as_view({"get": "list", "put": "set_survey"}),
        name="movies",
    ),
    path(
        "<int:movie_pk>/",
        views.MovieViewSet.as_view({"get": "retrieve", "post": "rate_movie"}),
        name="movie",
    ),
    path(
        "<int:movie_pk>/accounts/<str:username>/",
        views.MovieViewSet.as_view({"get": "get_rating"}),
        name="get_rating",
    ),
    path(
        "keywords/<int:pick_num>/",
        views.MovieViewSet.as_view({"get": "get_movies_with_keywords"}),
        name="get_movies_with_keywords",
    ),
]
