from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.cache import cache
from . import redis_key_schema

from django.shortcuts import get_object_or_404

from .models import Review, Comment

from .serializers import *


@api_view(['GET', 'POST'])
def index(request, cursor: int):

    if cursor == 0: cursor = Review.objects.all()[ : 1][0].id + 1

    def get_reviews():
        key = redis_key_schema.reviews(cursor)
        data = cache.get(key)

        if not data:
            reviews = Review.objects.cursor_paginated(cursor)
            data = ReviewListSerializer(reviews, many=True).data
            cache.set(key, data, timeout=12 * 60 * 60)
        return Response(data)

    def create_review():
        serializer = CreateReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        return get_reviews()
    elif request.method == 'POST':
        return create_review()


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def review(request, review_pk: int):

    review_obj = get_object_or_404(Review, pk=review_pk)
    
    def get_review_detail():
        serializer = ReviewSerializer(review_obj)
        return Response(serializer.data)

    def like_review():
        if review_obj.like_users.filter(username=request.user.username).exists():
            review_obj.like_users.remove(request.user)
            return Response({
                    'is_like': False,
                    'like_users_count': review_obj.like_users.count()
                })
        else:
            review_obj.like_users.add(request.user)
            return Response({
                    'is_like': True,
                    'like_users_count': review_obj.like_users.count()
                }, status=status.HTTP_201_CREATED)

    def update_review():
        if request.user == review_obj.user:
            serializer = ReviewSerializer(instance=review_obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    def delete_review():
        if request.user == review_obj.user:
            res = {
                'id': review_obj.id,
                'author': review_obj.user.username,
                'detail': 'Successfully deleted.'
            }
            review_obj.delete()
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        else: return Response({'detail': 'UNAUTHORIZED.'},
                                status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return get_review_detail()
    elif request.method == 'POST':
        return like_review()
    elif request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['POST'])
def create_comment(request, review_pk: int):
    review = get_object_or_404(Review, pk=review_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment(request, review_pk: int, comment_pk: int):
    review = get_object_or_404(Review, pk=review_pk)
    comment_obj = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment_obj.user:
            serializer = CommentSerializer(instance=comment_obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    def delete_comment():
        if request.user == comment_obj.user:
            res = {
                'id': comment_obj.id,
                'author': comment_obj.user.username,
                'detail': 'Successfully deleted.'
            }
            comment_obj.delete()
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()
