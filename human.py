from player import Player


class PlayerOne(Player):
    def __init__(self):
        self.score = 0
        super().__init__()

    def choosing_gesture(self):
