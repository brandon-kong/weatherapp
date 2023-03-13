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

import environ
env = environ.Env()
env.read_env()

from .models import SavedLocations, SavedLocation

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
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                savedList = SavedLocations.objects.create(user=user)
                savedList.save()
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
            try:
                savedList = SavedLocations.objects.get(user=user)
            except:
                savedList = SavedLocations.objects.create(user=user)
                savedList.save()
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
            
class addLocationToList(APIView):
    def post(self, request):
        try:
            token = request.headers.get('Authorization')
            location = request.data.get('location')
            if (token.startswith('Bearer ')):
                token = token[7:]
                userToken = Token.objects.get(key=token)
                savedUserLocations = SavedLocations.objects.get_or_create(user=userToken.user)
                formattedLocation = f'{location["properties"]["lat"]}' + ',' + f'{location["properties"]["lon"]}'
                try:
                    # already exists, so remove it
                    savedLocation = SavedLocation.objects.get(container=savedUserLocations[0], location=formattedLocation)
                    savedLocation.delete()
                except:
                    # if the user hasn't saved it, then save it
                    savedLocation = SavedLocation()
                    savedLocation.container = savedUserLocations[0]
                    savedLocation.location = formattedLocation
                    savedLocation.save()
                return Response({'detail': 'Success'}, status=status.HTTP_200_OK)
                
            else:
                return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
        
class getSavedLocations(APIView):
    def post(self, request):
        try:
            token = request.headers.get('Authorization')
            if (token.startswith('Bearer ')):
                token = token[7:]
                userToken = Token.objects.get(key=token)
                savedUserLocations = SavedLocations.objects.get(user=userToken.user)
                savedLocations = SavedLocation.objects.filter(container=savedUserLocations)
                locations = []
                for location in savedLocations:
                    locations.append(location.location)
                return Response({'locations': locations}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
        
class locationIsInList(APIView):
    def post(self, request):
        try:
            token = request.headers.get('Authorization')
            location = request.data.get('location')
            if (token.startswith('Bearer ')):
                token = token[7:]
                userToken = Token.objects.get(key=token)
                formattedLocation = f'{location["properties"]["lat"]}' + ',' + f'{location["properties"]["lon"]}'
                savedUserLocations = SavedLocations.objects.get(user=userToken.user)
                try:
                    savedLocations = SavedLocation.objects.get(container=savedUserLocations, location=formattedLocation)
                except:
                    savedLocations = None
                if (savedLocations):
                    return Response({'detail': True}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': False}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
        
class getAutocorrectQuery(APIView):
    def post(self, request):
        params={
            "q": request.data.get('query'),
            "key": env('GEOAPIFY_API_KEY')
        }
        url = f'https://api.geoapify.com/v1/geocode/autocomplete?text={params["q"]}&apiKey={params["key"]}'
        r = requests.get(url)
        if (r.status_code == 200):
            return Response(r.json(), status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        
class reverseGeocode(APIView):
    def post(self, request):
        params={
            "lat": request.data.get('lat'),
            "lon": request.data.get('lon'),
            "key": env('GEOAPIFY_API_KEY')
        }
        url = f'https://api.geoapify.com/v1/geocode/reverse?lat={params["lat"]}&lon={params["lon"]}&apiKey={params["key"]}'
        r = requests.get(url)
        if (r.status_code == 200):
            return Response(r.json(), status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
        
class getWeatherQuery(APIView):
    def post(self, request):
        params={
            "encoded": request.data.get('encoded'),
            "key": env('VISUALCROSSINGS_API_KEY')
        }
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{params["encoded"]}&key={params["key"]}'
        r = requests.get(url)
        if (r.status_code == 200):
            return Response(r.json(), status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)