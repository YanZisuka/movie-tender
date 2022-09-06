from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.core.cache import cache
from . import redis_key_schema

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import *

User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    def retrieve(self, request, username: str):
        key = redis_key_schema.user_profile(username)

        data = cache.get(key)

        if not data:
            user = get_object_or_404(User, username=username)
            data = UserSerializer(user).data
            data["followers"] = user.followers.all().values("id")
            cache.set(key, data, timeout=12 * 60 * 60)
        return Response(data)

    @action(detail=True, methods=["post"])
    def set_follow(self, request, username: str):
        key = redis_key_schema.user_profile(username)

        user = get_object_or_404(User, username=username)

        if request.user != user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                cache.delete(key)
                cache.delete(redis_key_schema.user_profile(request.user.username))
                return Response(
                    {
                        "is_following": False,
                        "followers_count": user.followers.count(),
                        "followings_count": user.followings.count(),
                    }
                )
            else:
                user.followers.add(request.user)
                cache.delete(key)
                cache.delete(redis_key_schema.user_profile(request.user.username))
                return Response(
                    {
                        "is_following": True,
                        "followers_count": user.followers.count(),
                        "followings_count": user.followings.count(),
                    },
                    status=status.HTTP_201_CREATED,
                )
        else:
            return Response(
                {"detail": "UNAUTHORIZED."}, status=status.HTTP_401_UNAUTHORIZED
            )

    def update(self, request, username: str):
        user = get_object_or_404(User, username=username)

        if request.user == user:
            serializer = UserSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(
                {"detail": "UNAUTHORIZED."}, status=status.HTTP_401_UNAUTHORIZED
            )

    def destroy(self, request, username: str):
        user = get_object_or_404(User, username=username)

        if request.user == user:
            res = {
                "id": user.pk,
                "username": user.username,
                "detail": "Successfully deleted.",
            }
            user.delete()
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"detail": "UNAUTHORIZED."}, status=status.HTTP_401_UNAUTHORIZED
            )
