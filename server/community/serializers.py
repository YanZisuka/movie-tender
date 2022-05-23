from rest_framework import serializers
from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'like_users', 'content', 'created_at', 'updated_at', 'comment_set',)
        read_only_fields = ('id', 'user', 'like_users', 'comment_set',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'like_users', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'user',)
