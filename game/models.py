from django.db.models import Model, CharField, TextChoices
from django.utils.translation import gettext_lazy as _

MAX_NUMBER_OF_GUESSES = 10


class GameStatus(TextChoices):
    PLAYING = 'P', _('Playing')
    PLAYER_WON = 'W', _('Player won')
    PLAYER_LOST = 'L', _('Player lost')


class Game(Model):
    code = CharField(max_length=4)
    status = CharField(max_length=1, choices=GameStatus.choices, default=GameStatus.PLAYING)

    @property
    def tries(self) -> int:
        return self.guesses.count()

    @property
    def tries_left(self) -> int:
        return MAX_NUMBER_OF_GUESSES - self.tries
