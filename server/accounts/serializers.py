from rest_framework import serializers

from django.contrib.auth import get_user_model
from movies.models import Movie

from dj_rest_auth.registration.serializers import RegisterSerializer
from community.serializers import ReviewSerializer


class CustomRegisterSerializer(RegisterSerializer):
    
    nickname = serializers.CharField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'nickname', 'followers_count', 'followings_count',
            'review_set', 'watch_movies', 'email', 'survey',
        )
        read_only_fields = ('id', 'username', 'review_set', 'watch_movies', 'survey',)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path',)
    
    review_set = ReviewSerializer(many=True, read_only=True)
    watch_movies = MovieSerializer(many=True, read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'survey',)
        read_only_fields = ('id', 'username',)
