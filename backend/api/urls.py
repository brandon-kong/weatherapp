from django.urls import path
from . import views

urlpatterns = [
    path(r'users', views.UserCreate.as_view(), name='account-create'),
    path(r'login', views.UserLogin.as_view(), name='account-login'),
    path(r'google-auth', views.GoogleView.as_view(), name='google-auth'),
]