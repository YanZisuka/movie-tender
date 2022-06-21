from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.cache import cache
from . import redis_key_schema

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import *


User = get_user_model()

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def profile(request, username: str):

    key = redis_key_schema.user_profile(username)
    
    def get_profile():
        data = cache.get(key)

        if not data:
            user = get_object_or_404(User, username=username)
            data = UserSerializer(user).data
            data['followers'] = user.followers.all().values('id')
            cache.set(key, data, timeout=12 * 60 * 60)
        return Response(data)
    
    def follow_user():
        user = get_object_or_404(User, username=username)

        if request.user != user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                cache.delete(key)
                cache.delete(redis_key_schema.user_profile(request.user.username))
                return Response({
                    'is_following': False,
                    'followers_count': user.followers.count(),
                    'followings_count': user.followings.count()
                })
            else:
                user.followers.add(request.user)
                cache.delete(key)
                cache.delete(redis_key_schema.user_profile(request.user.username))
                return Response({
                    'is_following': True,
                    'followers_count': user.followers.count(),
                    'followings_count': user.followings.count()
                }, status=status.HTTP_201_CREATED)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    def update_user():
        user = get_object_or_404(User, username=username)

        if request.user == user:
            serializer = UserSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    def delete_user():
        user = get_object_or_404(User, username=username)

        if request.user == user:
            res = {
                'id': user.id,
                'username': user.username,
                'detail': 'Successfully deleted.'
            }
            user.delete()
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        else: return Response({'detail': 'UNAUTHORIZED.'}, 
                                status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return get_profile()
    elif request.method == 'POST':
        return follow_user()
    elif request.method == 'PUT':
        return update_user()
    elif request.method == 'DELETE':
        return delete_user()
