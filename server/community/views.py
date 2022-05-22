from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Review, Comment
from .serializers import *


@api_view(['GET', 'POST'])
def index(request):

    def get_reviews():
        pass

    def create_review():
        pass
    
    if request.method == 'GET':
        return get_reviews()
    elif request.method == 'POST':
        return create_review()


@api_view(['GET', 'PUT', 'DELETE'])
def review(request, review_pk):
    
    def get_review_detail():
        pass

    def update_review():
        pass

    def delete_review():
        pass

    if request.method == 'GET':
        return get_review_detail()
    elif request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['POST'])
def create_comment(request, review_pk):
    pass


@api_view(['PUT', 'DELETE'])
def comment(request, review_pk, comment_pk):

    def update_comment():
        pass

    def delete_comment():
        pass

    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()
