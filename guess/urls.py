from django.urls import include, path
from rest_framework.routers import DefaultRouter

from guess.views import GuessViewSet

router = DefaultRouter()

router.register(r'guess', GuessViewSet, basename='guess')

urlpatterns = [
    path('', include(router.urls)),
]
