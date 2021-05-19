import random
import time
from player import Player


class AI(Player):
    def __init__(self):
        super().__init__()

    def gesture_selection(self):
        time.sleep(2)
        self.chosen_gesture = random.choice(self.list_of_gestures)
