class GameOverException(Exception):
    def __init__(self, message="This game is over!"):
        self.message = message
        super().__init__(self.message)
