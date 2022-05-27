import random

from django.shortcuts import get_object_or_404
from django.db.models import Sum

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
            movies = random.sample(list(Movie.objects.filter(keywords__overlap=[kwrd for kwrd in request.user.survey])), 10)
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else: return Response({
            'id': None,
            'detail': 'This user has no survey.'
            })

    def set_survey():
        validation = {'survey': []}
        for kwrd in request.data['survey']:
            if Keyword.objects.filter(keyword=kwrd).exists(): validation['survey'].append(kwrd)

        serializer = SurveySerializer(instance=request.user, data=validation)
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
            if Rating.objects.filter(user=request.user, movie=movie_obj).exists():

                movie_obj.vote_average = ((movie_obj.vote_average * movie_obj.vote_count) - Rating.objects.filter(user=request.user, movie=movie_obj).aggregate(Sum('rating'))['rating__sum']) / (movie_obj.vote_count - Rating.objects.filter(user=request.user, movie=movie_obj).count())
                movie_obj.vote_count -= Rating.objects.filter(user=request.user, movie=movie_obj).count()

                Rating.objects.filter(user=request.user, movie=movie_obj).delete()
            serializer.save(user=request.user, movie=movie_obj)

            # 영화 평점 재계산
            new_rating = ((movie_obj.vote_average * movie_obj.vote_count) + Rating.objects.filter(user=request.user, movie=movie_obj).aggregate(Sum('rating'))['rating__sum']) / (movie_obj.vote_count + 1)
            movie_obj.vote_average = round(new_rating, 1)
            movie_obj.vote_count += 1
            movie_obj.save(update_fields=['vote_count', 'vote_average'])

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return get_movie_detail()
    elif request.method == 'POST':
        return set_rating()


@api_view(['GET'])
def get_staff(request):
    staffs = random.sample(list(Staff.objects.filter(role='Actor')), 2)
    serializer = StaffSerializer(staffs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_genre(request, genre_group):
    movie = random.choice(Movie.objects.filter(genre_group=genre_group))
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def get_movies_with_keyword(request, pick_num):
    kwrds = [
        'anime', 'superhero', 'military', 'musical', 'school',
        'romance', 'army', 'space', 'future', 'mafia',
        'action', 'jazz', 'friendship', 'villain', 'elves',
        'dwarf', 'steampunk', 'time travel', 'based on novel or book',
    ]
    # kwrds = Keyword.objects.all().values('keyword')
    movies = random.sample(list(Movie.objects.filter(keywords__overlap=[kwrd for kwrd in kwrds])), pick_num)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
