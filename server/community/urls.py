from django.urls import path
from . import views


app_name = 'community'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='index'),
    path('<int:review_pk>/', views.ReviewView.as_view(), name='review'),
    path('<int:review_pk>/comments/', views.CommentView.as_view(), name='create_comment'),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.CommentView.as_view(), name='comment'),
]
