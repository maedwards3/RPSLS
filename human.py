from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def gesture_selection(self):
        print("Choose from the following gestures to make your move:")
        print("Enter <0> for Rock")
        print("Enter <1> for Paper")
        print("Enter <2> for Scissors")
        print("Enter <3> for Lizard")
        print("Enter <4> for Spock")
        print()
        human_selection = input()
        if int(human_selection) == 0:
            self.chosen_gesture = self.list_of_gestures[0]
            return self.chosen_gesture
        elif int(human_selection) == 1:
            self.chosen_gesture = self.list_of_gestures[1]
            return self.chosen_gesture
        elif int(human_selection) == 2:
            self.chosen_gesture = self.list_of_gestures[2]
            return self.chosen_gesture
        elif int(human_selection) == 3:
            self.chosen_gesture = self.list_of_gestures[3]
            return self.chosen_gesture
        elif int(human_selection) == 4:
            self.chosen_gesture = self.list_of_gestures[4]
            return self.chosen_gesture
        print()
