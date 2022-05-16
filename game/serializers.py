"""Game serializers module"""
from rest_framework.serializers import ModelSerializer

from game.models import Game
from guess.serializers import GuessSerializer


class GameSerializer(ModelSerializer):
    """
    Game serializer to define API requests.
    """
    guesses = GuessSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'code', 'guesses', 'status', 'tries_left']
        read_only_fields = ['id', 'guesses', 'status', 'tries_left']
