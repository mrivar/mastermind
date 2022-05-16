"""Guess tests module"""
from unittest.mock import MagicMock, patch, PropertyMock

from django.test import TestCase

from game.exceptions import GameOverException
from game.models import Game
from guess.models import Guess


class GuessTestCase(TestCase):
    """
     Class to test the guess model
     """
    GAME_CODE = 'ABCD'
    # Guesses in the format (guess code, black pegs, white pegs)
    GUESSES = [('ABCD', 4, 0), ('BCAA', 0, 3), ('DCBA', 0, 4), ('ACBB', 1, 2), ('EFCA', 1, 1),
               ('DDDD', 1, 0), ('AAAA', 1, 0), ('BBBB', 1, 0), ('YYYY', 0, 0), ('ABDY', 2, 1)]

    def setUp(self):
        self.game = Game.objects.create(code=self.GAME_CODE)

    def test_compute_pegs_with_same_code(self):
        """
        Test that a guess with the same guess code as the game code returns 4 black pegs and 0 white pegs
        """
        test_guess = Guess(code=self.game.code, game=self.game)
        black_pegs, white_pegs = test_guess.compute_pegs()
        self.assertEqual(black_pegs, 4)
        self.assertEqual(white_pegs, 0)

    def test_compute_pegs_with_set_of_codes(self):
        """
        Test the result of computing pegs given a set of guesses with its respective black and white pegs
        """
        for guess in self.GUESSES:
            guess_code, black_pegs_expected, white_pegs_expected = guess
            test_guess = Guess(code=guess_code, game=self.game)
            black_pegs, white_pegs = test_guess.compute_pegs()
            self.assertEqual(black_pegs, black_pegs_expected)
            self.assertEqual(white_pegs, white_pegs_expected)

    def test_compute_pegs_runs_when_saving_or_updating_model(self):
        """
        Test that the function to compute pegs is run when the model is saved or updated and the game isn't over
        """
        with patch('guess.models.Game.is_over', new_callable=PropertyMock) as mock_is_over:
            mock_is_over.return_value = False
            test_guess = Guess(code=self.GAME_CODE, game=self.game)
            test_guess.compute_pegs = MagicMock(return_value=(1, 0))
            test_guess.save()
            test_guess.compute_pegs.assert_called_once()
            self.assertEqual(test_guess.black_pegs, 1)
            self.assertEqual(test_guess.white_pegs, 0)

    def test_checking_the_game_status_runs_when_saving_or_updating_model(self):
        """
        Test that the function to check game status is run when the model is saved or updated and the game isn't over
        """
        with patch('guess.models.Game.is_over', new_callable=PropertyMock) as mock_is_over:
            mock_is_over.return_value = False
            test_guess = Guess(code=self.GAME_CODE, game=self.game)
            test_guess.game.check_game_status = MagicMock()
            test_guess.save()
            test_guess.game.check_game_status.assert_called_once()

    def test_compute_pegs_runs_when_the_game_is_over_the_model_isnt_saved(self):
        """
        Test that when the game is over the guess isn't saved
        """
        with self.assertRaises(GameOverException):
            with patch('guess.models.Game.is_over', new_callable=PropertyMock) as mock_is_over:
                mock_is_over.return_value = True
                test_guess = Guess(code=self.GAME_CODE, game=self.game)
                test_guess.save()
