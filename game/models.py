from django.db.models import Model, CharField, TextChoices
from django.utils.translation import gettext_lazy as _

from mastermind.config import MAX_NUMBER_OF_GUESSES, GAME_CODE_LENGTH


class GameStatus(TextChoices):
    PLAYING = 'P', _('Playing')
    PLAYER_WON = 'W', _('Player won')
    PLAYER_LOST = 'L', _('Player lost')


class Game(Model):
    code = CharField(max_length=GAME_CODE_LENGTH)
    status = CharField(max_length=1, choices=GameStatus.choices, default=GameStatus.PLAYING)

    @property
    def tries(self) -> int:
        return self.guesses.count()

    @property
    def tries_left(self) -> int:
        return MAX_NUMBER_OF_GUESSES - self.tries

    @property
    def is_over(self):
        return self.status != GameStatus.PLAYING

    def check_game_status(self):
        if len(self.guesses.filter(black_pegs=GAME_CODE_LENGTH)) > 0:
            self.status = GameStatus.PLAYER_WON
        elif self.tries_left == 0:
            self.status = GameStatus.PLAYER_LOST
        else:
            self.status = GameStatus.PLAYING
        self.save()
