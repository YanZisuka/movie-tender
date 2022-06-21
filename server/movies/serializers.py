from rest_framework import serializers

from .models import Movie, Staff, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id', 'tmdb_id', 'title', 'adult', 'release_date', '_genres',
            'runtime', 'overview', 'vote_average', 'credits',
            'rating_users', 'poster_path', 'video_path', '_providers',
            )

    class StaffSerializer(serializers.ModelSerializer):
        class Meta:
            model = Staff
            fields = ('id', 'tmdb_id', 'name', 'role',)

    credits = StaffSerializer(many=True)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average', 'overview', 'poster_path', '_keywords',)


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'tmdb_id', 'name', 'profile_path',)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'movie', 'rating',)
        read_only_fields = ('id', 'user', 'movie',)
