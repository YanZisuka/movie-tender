from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import *


@api_view(['POST'])
def index(request):

    def signup():
        pass
    
    if request.method == 'POST':
        return signup()


@api_view(['POST'])
def login(request):
    pass


@api_view(['POST'])
def logout(request):
    pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def profile(request, username):
    
    def get_profile():
        pass
    
    def follow_user():
        pass

    def update_user():
        pass

    def delete_user():
        pass

    if request.method == 'GET':
        return get_profile()
    elif request.method == 'POST':
        return follow_user()
    elif request.method == 'PUT':
        return update_user()
    elif request.method == 'DELETE':
        return delete_user()
