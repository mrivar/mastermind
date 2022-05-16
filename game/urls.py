"""Game urls module"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from game.views import GameViewSet

ROUTER = DefaultRouter()
ROUTER.register(r'game', GameViewSet, basename='game')

urlpatterns = [
    path('', include(ROUTER.urls)),
]
