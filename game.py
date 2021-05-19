import time
from player import Player
from human import Human
from artificial_intelligence import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Player()

    def run_game(self):
        time.sleep(1)
        print()
        self.player_one.name = input("What is your name?")
        print()
        print(f"Welcome {self.player_one}, to Rock, Paper, Scissors...Lizard, Spock!")
        print()
        print("*************************************************")
        print()
        user_input = True
        while user_input:
            rule_check = input("Would you like to look at the rules?")
            print()
            print("*************************************************")
            if rule_check.lower() == "yes":
                print()
                self.game_rules()
            elif rule_check.lower() == "no":
                print()
                print("Now to select player two.")
                self.choose_player_two()
            else:
                print("Please enter yes or no.")
                continue

    def game_rules(self):
        print("The rules are simple:")
        print("Rock crushes Scissors")
        print("Scissors cuts paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print()
        print("Player one will start the round by picking a gesture, followed by player two picking a gesture.")
        print("One player will win the round based on each player's gesture choice. Or that round will result in a "
              "tie if the same gesture is picked by both players, and no player will get a point that round.")
        print("First person to win 3 total rounds wins the game!")
        print()
        time.sleep(8)
        done_reading_rules = True
        while done_reading_rules:
            exit_rules = input("Are you ready to play the game?")
            print()
            print("*************************************************")
            if exit_rules.lower() == "yes":
                print()
                print("Now to select player two.")
                self.choose_player_two()
            else:
                continue

    def choose_player_two(self):
        self.player_two = input("Select <1> to play against another human, or <2> to play against the computer.")
        if int(self.player_two) == 1:
            self.player_two = Human()
            self.player_two.name = input("What is player two's name?")
            print(f"Time for {self.player_one.name} to play {self.player_two.name} in RPSLS!")
            print()
            print("*************************************************")
            print()
            self.start_game()
            return self.player_two.name
        elif int(self.player_two) == 2:
            self.player_two = AI()
            self.player_two.name = "Computer"
            print(f"You have selected to play against the {self.player_two.name}.")
            print("Let's begin!")
            print()
            print("*************************************************")
            print()
            self.start_game()
            return self.player_two.name

    def start_game(self):
        while self.player_two.score < 3 or self.player_two.score < 3:
            print(f"{self.player_one.name} goes first.")
            self.human_vs_human_game_rounds()

    # def human_vs_human_game_rounds(self):
    #     self.player_two = Human()
    #     self.player_one.sentient_gesture()
    #     print(f"{self.player_one.name} made {self.player_one.chosen_gesture}.")
    #     self.player_two.sentient_gesture()
    #     print(f"{self.player_two.name} made {self.player_two.chosen_gesture}.")
    #     if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
    #         print(f"Both players made {self.player_one.chosen_gesture}. Tie round.")
    #     elif self.player_one.chosen_gesture == self.player_one.list_of_gestures[0]:
    #         if self.player_two.chosen_gesture == self.player_two.list_of_gestures[1]:
