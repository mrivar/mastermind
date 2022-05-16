from rest_framework.serializers import ModelSerializer

from guess.models import Guess


class GuessSerializer(ModelSerializer):
    """
    Guess serializer to define API requests.
    """

    class Meta:
        model = Guess
        fields = ['id', 'code', 'game', 'black_pegs', 'white_pegs']
        read_only_fields = ['id', 'black_pegs', 'white_pegs']
