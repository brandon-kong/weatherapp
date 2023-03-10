from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import HttpResponse

from django.views.decorators.csrf import ensure_csrf_cookie
from social_django.utils import psa

import requests
# Class based view to Get User Details using Token Authentication

class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
    
class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    """
    Returns the user session.
    """
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            print('HIIII')
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UserSession(APIView):
    """
    Returns the user session.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    
class GoogleView(APIView):
    def post(self, request):
        serializer = SocialSerializer(data=request.data)
        code = request.data.get('code')
        params={
            "code": code,
            "client_id": "396604274247-2gs6m177f9ajj2km4qhjplcmrgmkkp5l.apps.googleusercontent.com",
            "client_secret": "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",
            "redirect_uri": "http://localhost:8081",
            "grant_type": "authorization_code"
        }
        r = requests.post('https://oauth2.googleapis.com/token', params=params)
        print(request)
        if 'token' in request.COOKIES:
            return Response({'detail': 'You are already logged in!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if (r.status_code == 200):
                data = r.json()
                endpoint = Response(data, status=status.HTTP_200_OK)
                endpoint.set_cookie('token', data['access_token'])
                return endpoint
            else:
                return Response(r.json(), status=status.HTTP_400_BAD_REQUEST)