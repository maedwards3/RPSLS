import random
from player import Player


class AI(Player):
    def __init__(self):
        super().__init__()

    def gesture_selection(self):
        random.choice(self.list_of_gestures)
