from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'nickname', 'followers_count', 'followings_count',
            'review_set', 'watch_movies', 'email', 'survey',
        )
        read_only_fields = ('id', 'username', 'review_set', 'watch_movies', 'survey',)


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'survey',
        )
        read_only_fields = ('id', 'username',)
