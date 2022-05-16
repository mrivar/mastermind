from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from guess.models import Guess
from guess.serializers import GuessSerializer


class GuessViewSet(mixins.CreateModelMixin,
                   GenericViewSet):
    """
    Guess API views. Only allows POST requests.
    """
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

