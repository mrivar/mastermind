"""Game exceptions module"""


class GameOverException(Exception):
    """
    Exception to handle when a game is over
    """
    def __init__(self, message="This game is over!"):
        self.message = message
        super().__init__(self.message)
