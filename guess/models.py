from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField

from game.models import Game


class Guess(Model):
    code = CharField(max_length=4)
    game = ForeignKey(to=Game, on_delete=CASCADE, related_name='guesses')
    white_pins = IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])
    black_pins = IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)])

    def _compute_pins(self):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        self._compute_pins()
        return super().save(*args, **kwargs)
