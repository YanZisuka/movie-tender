import random

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Staff, Rating, Keyword
from .serializers import *
from accounts.serializers import SurveySerializer


@api_view(['GET', 'PUT'])
def index(request):

    def get_recommendations():
        if request.user.survey:
            movies = Movie.objects.filter(keywords__contains=[])
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else: return Response({
            'id': None,
            'detail': 'This user has no survey.'
            })

    def set_survey():
        serializer = SurveySerializer(instance=request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'GET':
        return get_recommendations()
    elif request.method == 'PUT':
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
            serializer.save(user=request.user, movie=movie_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return get_movie_detail()
    elif request.method == 'POST':
        return set_rating()


@api_view(['GET'])
def genre(request, genre_group):
    movie = random.choice(Movie.objects.filter(genre_group=genre_group))
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def keyword(request, keyword_pk):
    kwrd = Keyword.objects.get(pk=keyword_pk)
    movie = random.choice(Movie.objects.filter(keywords__contains=[kwrd.keyword]))
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)
