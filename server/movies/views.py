from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Staff, Rating, Keyword
from .serializers import *


@api_view(['GET', 'POST'])
def index(request):

    def get_recommendations():
        pass

    def set_survey():
        pass
    
    if request.method == 'GET':
        return get_recommendations()
    elif request.method == 'POST':
        return set_survey()


@api_view(['GET', 'POST'])
def movie(request, movie_pk):
    
    def get_movie_detail(request):
        pass

    def set_grade(request):
        pass

    if request.method == 'GET':
        return get_movie_detail()
    elif request.method == 'POST':
        return set_grade()


@api_view(['GET'])
def genre(request, genre_group):
    pass


@api_view(['GET'])
def keyword(request, keyword):
    pass
