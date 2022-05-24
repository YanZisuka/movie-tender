from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


User = get_user_model()

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def profile(request, username):

    user = get_object_or_404(User, username=username)
    
    def get_profile():
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def follow_user():
        if request.user != user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                return Response({
                    'is_following': False,
                    'followers_count': user.followers.count(),
                    'followings_count': user.followings.count()
                })
            else:
                user.followers.add(request.user)
                return Response({
                    'is_following': True,
                    'followers_count': user.followers.count(),
                    'followings_count': user.followings.count()
                })
        else: return Response({'detail': 'BAD REQUEST.'}, status=status.HTTP_400_BAD_REQUEST)

    def update_user():
        if request.user == user:
            serializer = UserSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else: return Response({'detail': 'BAD REQUEST.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete_user():
        if request.user == user:
            res = {
                'id': user.id,
                'username': user.username,
                'detail': 'Successfully deleted.'
            }
            user.delete()
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        else: return Response({'detail': 'BAD REQUEST.'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return get_profile()
    elif request.method == 'POST':
        return follow_user()
    elif request.method == 'PUT':
        return update_user()
    elif request.method == 'DELETE':
        return delete_user()
