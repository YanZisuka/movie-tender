from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path(
        "profile/<str:username>/",
        views.UserViewSet.as_view(
            {
                "get": "retrieve",
                "post": "set_follow",
                "put": "update",
                "delete": "destroy",
            }
        ),
        name="profile",
    ),
]
