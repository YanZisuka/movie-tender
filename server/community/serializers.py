from re import M
from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model


class ReviewSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname',  )
        user = UserSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = '__all__'

    class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname',  )

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', )

    comment_set = CommentSerializer(many=True, read_only=True)
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'like_users', 'content', 'created_at', 'updated_at','comment_set', 'movie')
        read_only_fields = ('id', 'user', 'like_users','comment_set', 'movie')

class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'like_users', 'content', 'created_at', 'updated_at','comment_set', 'movie')
        read_only_fields = ('id', 'user', 'like_users','comment_set', )

class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname',  )
        
    user = UserSerializer(read_only=True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', )
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'like_users', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'user',)
