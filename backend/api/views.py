from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from google.oauth2 import id_token
from google.auth.transport import requests

# Class based view to Get User Details using Token Authentication
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
        token = {'code': request.data.get('code')}
        print(token)

        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token['id_token'], requests.Request(), '396604274247-2gs6m177f9ajj2km4qhjplcmrgmkkp5l.apps.googleusercontent.com')
            print(idinfo)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            return Response(idinfo)
        except ValueError as err:
            # Invalid token
            print(err)
            content = {'message': 'Invalid token'}
            return Response(content)