from rest_framework import status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.cache import cache
from . import redis_key_schema

from django.shortcuts import get_object_or_404

from .models import Review, Comment

from .serializers import *


class ReviewListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        cursor: int = int(request.GET.get('cursor'))
        if cursor == 0: cursor = Review.objects.all()[ : 1][0].id + 1
        key = redis_key_schema.reviews(cursor)
        data = cache.get(key)

        if not data:
            reviews = Review.objects.cursor_paginated(cursor)
            data = ReviewListSerializer(reviews, many=True).data
            cache.set(key, data, timeout=12 * 60 * 60)
        return Response(data)

    def post(self, request):
        serializer = CreateReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)


class ReviewView(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, review_pk: int):
        review_obj = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review_obj)
        return Response(serializer.data)

    def post(self, request, review_pk: int):
        review_obj = get_object_or_404(Review, pk=review_pk)

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

    def put(self, request, review_pk: int):
        review_obj = get_object_or_404(Review, pk=review_pk)

        if request.user == review_obj.user:
            serializer = ReviewSerializer(instance=review_obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, review_pk: int):
        review_obj = get_object_or_404(Review, pk=review_pk)

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


class CommentView(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, review_pk:int):
        review = get_object_or_404(Review, pk=review_pk)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

    def put(self, request, review_pk:int, comment_pk: int):
        review = get_object_or_404(Review, pk=review_pk)
        comment_obj = get_object_or_404(Comment, pk=comment_pk)

        if request.user == comment_obj.user:
            serializer = CommentSerializer(instance=comment_obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, review_pk:int, comment_pk: int):
        review = get_object_or_404(Review, pk=review_pk)
        comment_obj = get_object_or_404(Comment, pk=comment_pk)

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
