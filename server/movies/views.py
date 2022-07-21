import random

from rest_framework import status, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.cache import cache
from . import redis_key_schema

from django.shortcuts import get_object_or_404
from django.db.models import Sum

from django.contrib.auth import get_user_model
from .models import Movie, Staff, Rating, Keyword

from .serializers import *
from accounts.serializers import SurveySerializer


class MovieListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request):
        if request.user.survey:
            key = redis_key_schema.movies_for_user(request.user)
            data = cache.get(key)

            if not data:
                movies = list(Movie.objects.filter(_keywords__overlap=[kwrd for kwrd in request.user.survey]))
                data = MovieSerializer(movies, many=True).data
                cache.set(key, data, timeout=24 * 60 * 60)
            return Response(random.sample(data, 10))

        else:
            return Response({'detail': 'This user has no survey.'}, 
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        validation = {'survey': []}
        for kwrd in request.data['survey']:
            if Keyword.objects.filter(keyword=kwrd).exists(): validation['survey'].append(kwrd)

        serializer = SurveySerializer(instance=request.user, data=validation)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            cache.delete(redis_key_schema.movies_for_user(request.user))
            return Response(serializer.data)


class MovieView(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, movie_pk: int):
        key = redis_key_schema.movie_detail(movie_pk)
        data = cache.get(key)

        if not data:
            movie_obj = get_object_or_404(Movie, pk=movie_pk)
            data = MovieSerializer(movie_obj).data
            cache.set(key, data, timeout=7 * 24 * 60 * 60)
        return Response(data)

    def post(self, request, movie_pk: int):
        movie_obj = get_object_or_404(Movie, pk=movie_pk)

        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if Rating.objects.filter(user=request.user, movie=movie_obj).exists():
                
                # 영화 평점 복구
                numerator = (movie_obj.vote_average * movie_obj.vote_count) - Rating.objects.filter(user=request.user, movie=movie_obj).aggregate(Sum('rating'))['rating__sum']
                denominator = movie_obj.vote_count - Rating.objects.filter(user=request.user, movie=movie_obj).count()
                
                movie_obj.vote_average = (numerator / denominator) if denominator != 0 else 0
                movie_obj.vote_count -= Rating.objects.filter(user=request.user, movie=movie_obj).count()

                Rating.objects.filter(user=request.user, movie=movie_obj).delete()
            serializer.save(user=request.user, movie=movie_obj)

            # 영화 평점 재계산
            numerator = (movie_obj.vote_average * movie_obj.vote_count) + Rating.objects.filter(user=request.user, movie=movie_obj).aggregate(Sum('rating'))['rating__sum']
            movie_obj.vote_count += 1

            new_rating = numerator / movie_obj.vote_count
            movie_obj.vote_average = round(new_rating, 1)
            movie_obj.save(update_fields=['vote_count', 'vote_average'])

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_rating(request, movie_pk: int, username: str):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), username=username)

    if Rating.objects.filter(movie=movie, user=user).exists():
        rating = get_object_or_404(Rating, movie=movie, user=user)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    else: return Response({
        'user': user.id,
        'movie': movie.id,
        'rating': 0
    })


@api_view(['GET'])
def get_staff(request):
    staffs = random.sample(list(Staff.objects.filter(role='Actor')), 2)
    serializer = StaffSerializer(staffs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_genre(request, genre_group: str):
    movie = random.choice(Movie.objects.filter(genre_group=genre_group))
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def get_movies_with_keywords(request, pick_num: int):
    key = redis_key_schema.movies()
    data = cache.get(key)

    if not data:
        kwrds = [
            'anime', 'superhero', 'military', 'musical', 'school',
            'romance', 'army', 'space', 'future', 'mafia',
            'action', 'jazz', 'friendship', 'villain', 'elves',
            'dwarf', 'steampunk', 'time travel', 'based on novel or book',
        ]
        movies = list(Movie.objects.filter(_keywords__overlap=[kwrd for kwrd in kwrds]))
        data = MovieListSerializer(movies, many=True).data
        cache.set(key, data, timeout=2 * 24 * 60 * 60)
    return Response(random.sample(data, pick_num))
