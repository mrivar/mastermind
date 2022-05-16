from unittest.mock import MagicMock, patch, PropertyMock

from django.test import TestCase

from game.models import Game, GameStatus


class GameTestCase(TestCase):
    GAME_CODE = 'ABCD'

    def setUp(self):
        self.game = Game.objects.create(code=self.GAME_CODE)

    def test_check_game_status_runs_save_function(self):
        """
        Test checking game status executes the save function to properly change the status
        """
        self.game.save = MagicMock()
        self.game.check_game_status()
        self.game.save.assert_called_once()

    def test_check_game_status_is_player_won_if_there_is_a_correct_guess(self):
        """
        Test checking game status changes the status to player won if there is a correct guess
        """
        with patch('game.models.Game._correct_guesses', new_callable=PropertyMock) as mock_correct_guesses:
            mock_correct_guesses.return_value = [1]
            self.game.check_game_status()
            self.assertTrue(self.game.is_over)
            self.assertEqual(self.game.status, GameStatus.PLAYER_WON)

    def test_check_game_status_is_player_lost_if_there_is_no_correct_guess_and_no_more_tries(self):
        """
        Test checking game status changes the status to player lost if there are no correct guess and no more tries
        """
        with patch('game.models.Game._correct_guesses', new_callable=PropertyMock) as mock_correct_guesses:
            with patch('game.models.Game.tries_left', new_callable=PropertyMock) as mock_tries_left:
                mock_correct_guesses.return_value = []
                mock_tries_left.return_value = 0
                self.game.check_game_status()
                self.assertTrue(self.game.is_over)
                self.assertEqual(self.game.status, GameStatus.PLAYER_LOST)

    def test_check_game_status_is_playing_if_there_is_no_correct_guess_and_there_are_tries_left(self):
        """
        Test checking game status changes the status to player lost if there are no correct guess and no more tries
        """
        with patch('game.models.Game._correct_guesses', new_callable=PropertyMock) as mock_correct_guesses:
            with patch('game.models.Game.tries_left', new_callable=PropertyMock) as mock_tries_left:
                mock_correct_guesses.return_value = []
                mock_tries_left.return_value = 1
                self.game.check_game_status()
                self.assertFalse(self.game.is_over)
                self.assertEqual(self.game.status, GameStatus.PLAYING)
