from rest_framework.serializers import HyperlinkedModelSerializer

from game.models import Game


class GameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'code', 'guesses', 'status', 'tries_left']
        read_only_fields = ['id', 'guesses', 'status', 'tries_left']
