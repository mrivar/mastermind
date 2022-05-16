"""Guess models module"""
import uuid
from typing import Tuple

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField, UUIDField

from game.exceptions import GameOverException
from game.models import Game
from mastermind.settings import GAME_CODE_LENGTH


class Guess(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = CharField(max_length=GAME_CODE_LENGTH)
    game = ForeignKey(to=Game, on_delete=CASCADE, related_name='guesses')
    black_pegs = IntegerField(validators=[MaxValueValidator(GAME_CODE_LENGTH), MinValueValidator(0)])
    white_pegs = IntegerField(validators=[MaxValueValidator(GAME_CODE_LENGTH), MinValueValidator(0)])

    def compute_pegs(self) -> Tuple[int, int]:
        """
        Compute the number of black pegs in a Mastermind game guess given the secret code and the guess

        Returns:
            Number of black pegs and white pegs
        """
        black_pegs, secret_code_dict, guess_code_dict = self.__compute_black_pegs(secret_code=self.game.code,
                                                                                  guess_code=self.code)
        white_pegs = self.__compute_white_pegs(secret_code=secret_code_dict, guess_code=guess_code_dict)
        return black_pegs, white_pegs

    @staticmethod
    def __compute_black_pegs(secret_code: str, guess_code: str) -> Tuple[int, dict, dict]:
        """
        Compute the number of black pegs in a Mastermind game guess given the secret code and the guess

        Parameters:
            secret_code: string with the secret code of the game
            guess_code: string with the guess entered by the user

        Returns:
            Number of black pegs, and modified codes as count dictionaries without the exact guesses
        """
        new_secret_code = dict()
        new_guess_code = dict()
        black_pegs = 0
        for code, guess in zip(secret_code, guess_code):
            if code == guess:
                black_pegs += 1
            else:
                new_secret_code[code] = new_secret_code.get(code, 0) + 1
                new_guess_code[guess] = new_guess_code.get(guess, 0) + 1
        return black_pegs, new_secret_code, new_guess_code

    @staticmethod
    def __compute_white_pegs(secret_code: dict, guess_code: dict) -> int:
        """
        Compute the number of white pegs in a Mastermind game guess given the secret code and the guess
        without the values of the exact guesses as dictionaries with the count of values

        Parameters:
            secret_code: dictionary with the count of values in the secret code of the game without the exact guesses
            guess_code: dictionary with the count of values in the guess entered by the user without the exact guesses

        Returns:
            Number of white pegs
        """
        white_pegs = 0
        for guess in guess_code:
            if secret_code.get(guess):
                white_pegs += 1
                secret_code[guess] -= 1
        return white_pegs

    def save(self, *args, **kwargs):
        if self.game.is_over:
            raise GameOverException

        self.black_pegs, self.white_pegs = self.compute_pegs()
        super().save(*args, **kwargs)
        self.game.check_game_status()
