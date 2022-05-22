from django.urls import path
from . import views


app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:review_pk>/', views.review, name='review'),
    path('<int:review_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.comment, name='comment'),
]
