from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("profile/<str:username>/", views.UserView.as_view(), name="profile"),
]
