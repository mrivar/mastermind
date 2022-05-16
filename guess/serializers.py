from rest_framework.serializers import ModelSerializer

from game.exceptions import GameOverException
from game.models import Game
from guess.models import Guess


class GuessSerializer(ModelSerializer):
    """
    Guess serializer to define API requests.
    """

    class Meta:
        model = Guess
        fields = ['id', 'code', 'game', 'black_pegs', 'white_pegs']
        read_only_fields = ['id', 'black_pegs', 'white_pegs']

    def create(self, validated_data):
        game: Game = validated_data['game']
        if not game.is_over:
            instance: Guess = super().create(validated_data)
        else:
            raise GameOverException
        game.check_game_status()
        return instance
