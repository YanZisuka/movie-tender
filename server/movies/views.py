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

    movie_obj = get_object_or_404(Movie, pk=movie_pk)
    
    def get_movie_detail():
        serializer = MovieSerializer(movie_obj)
        return Response(serializer.data)

    def set_rating():
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return get_movie_detail()
    elif request.method == 'POST':
        return set_rating()


@api_view(['GET'])
def genre(request, genre_group):
    pass


@api_view(['GET'])
def keyword(request, keyword):
    pass
