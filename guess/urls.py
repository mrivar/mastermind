"""Guess urls module"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from guess.views import GuessViewSet

ROUTER = DefaultRouter()

ROUTER.register(r'guess', GuessViewSet, basename='guess')

urlpatterns = [
    path('', include(ROUTER.urls)),
]
