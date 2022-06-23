from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Review, Comment
from movies.models import Movie


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'like_users', 'content', 'created_at', 'updated_at', 'is_modified', 'comment_set',)
        read_only_fields = ('id', 'user', 'movie', 'like_users', 'is_modified', 'comment_set',)

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'user', 'review', 'content', 'created_at', 'is_modified',)
            read_only_fields = ('is_modified',)

        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname',)

        user = UserSerializer(read_only=True)

    class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname',)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path',)

    comment_set = CommentSerializer(many=True, read_only=True)
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'like_users', 'content', 'created_at', 'updated_at', 'comment_set',)
        read_only_fields = ('id', 'user', 'like_users', 'comment_set',)


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'like_users', 'content', 'comment_set',)

    class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname',)
        
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path',)

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'user', 'review', 'content', 'created_at', 'is_modified',)
            read_only_fields = ('is_modified',)

        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username', 'nickname',)

        user = UserSerializer(read_only=True)

    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'review', 'content', 'created_at', 'updated_at', 'is_modified',)
        read_only_fields = ('id', 'user', 'review', 'is_modified',)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname',)

    user = UserSerializer(read_only=True)
