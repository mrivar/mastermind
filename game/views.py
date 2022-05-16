"""Games views module"""
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from game.models import Game
from game.serializers import GameSerializer


class GameViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """
    Game API views. Allow GET and POST requests.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
