from django.urls import path
from . import views

urlpatterns = [
    path(r'users', views.UserCreate.as_view(), name='account-create'),
    path(r'login', views.UserLogin.as_view(), name='account-login'),
    path(r'google-auth', views.GoogleView.as_view(), name='google-auth'),
    path(r'add-location', views.addLocationToList.as_view(), name='add-location'),
    path(r'get-saved-locations', views.getSavedLocations.as_view(), name='get-saved-locations'),
    path(r'location-is-in-list', views.locationIsInList.as_view(), name='location-is-in-list'),
    path(r'autocomplete', views.getAutocorrectQuery.as_view(), name='autocorrect'),
    path(r'reverse-geocode', views.reverseGeocode.as_view(), name='reverse-geocode'),
    path(r'weather', views.getWeatherQuery.as_view(), name='weather'),
]