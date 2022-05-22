from rest_framework import serializers
from .models import Movie, Staff, Rating, Keyword


class MovieSerializer(serializers.ModelSerializer):

    class StaffSerializer(serializers.ModelSerializer):

        class Meta:
            model = Staff
            fields = ('name', 'character', 'role',)

    class Meta:
        model = Movie
        fields = (
            'title', 'adult', 'release_date', 'genres',
            'runtime', 'overview', 'vote_average', 'credits',
            'rating', 'poster_path', 'video_path', 'providers',
            )


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'title', 'vote_average', 'overview', 'poster_path',
        )


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = (
            'name', 'profile_path',
        )
