import time
from artificial_intelligence import AI


class Game:
    def __init__(self):
        self.player_one = ""
        self.player_two = ""

    def run_game(self):
        time.sleep(1)
        print()
        self.player_one = input("What is your name?")
        print()
        print(f"Welcome {self.player_one}, to Rock, Paper, Scissors...Lizard, Spock!")
        print()
        print("*************************************************")
        print()
        user_input = True
        while user_input:
            rule_check = input("Would you like to look at the rules?")
            if rule_check.lower() == "yes":
                print()
                self.game_rules()
            elif rule_check.lower() == "no":
                print()
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
        # time.sleep(8)
        exit_rules = input("Are you ready to play the game?")
        while exit_rules.lower() == "no":
            if exit_rules.lower() == "yes":
                print()
                self.choose_player_two()
            else:
                exit_rules = input("Are you ready to play the game?")

    def choose_player_two(self):
        self.player_two = input("Select <1> to play against another human, or <2> to play against the computer.")
        if int(self.player_two) == 1:
            self.player_two = input("What is player two's name?")
            print(f"Time for {self.player_one} to play {self.player_two} in RPSLS!")
        elif int(self.player_two) == 2:
            self.player_two = AI()
            print("You have selected to play against the computer.")
        # self.start_rounds()

    # def start_rounds(self):
    #     while self.player_one