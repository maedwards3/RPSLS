import time
from human import Human
from artificial_intelligence import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        time.sleep(1)
        print()
        self.player_one.name = input("What is your name?")
        print()
        print(f"Welcome {self.player_one.name}, to Rock, Paper, Scissors...Lizard, Spock!")
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
        user_input = input("Select <1> to play against another human, or <2> to play against the computer.")
        if int(user_input) == 1:
            self.player_two = Human()
            self.player_two.name = input("What is player two's name?")
            print(f"Time for {self.player_one.name} to play {self.player_two.name} in RPSLS!")
            print()
            print("*************************************************")
            print()
            self.start_game()
            return self.player_two.name
        elif int(user_input) == 2:
            self.player_two = AI()
            self.player_two.name = "Computer"
            print(f"You have selected to play against the Computer.")
            print("Let's begin!")
            print()
            print("*************************************************")
            print()
            self.start_game()
            return self.player_two.name

    def start_game(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            print(f"{self.player_one.name} goes first.")
            self.game_rounds()
        
    def game_rounds(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_one.gesture_selection()
            print(f"{self.player_one.name} used {self.player_one.chosen_gesture}.")
            print("--------------------")
            self.player_two.gesture_selection()
            print(f"{self.player_two.name} used {self.player_two.chosen_gesture}.")
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print(f"Both players used {self.player_one.chosen_gesture}. Tie round.")
                print()
                print("*************************************************")
                print()
            elif self.player_one.chosen_gesture == "Rock":
                if self.player_two.chosen_gesture == "Scissors":
                    print(f"Rock crushes Scissor. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Lizard":
                    print(f"Rock crushes Lizard. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Spock":
                    print(f"Spock vaporizes Rock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Paper":
                    print(f"Paper covers Rock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
            elif self.player_one.chosen_gesture == "Paper":
                if self.player_two.chosen_gesture == "Rock":
                    print(f"Paper covers Rock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Spock":
                    print(f"Paper disproves Spock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Scissors":
                    print(f"Scissors cuts Paper. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Lizard":
                    print(f"Lizard eats Paper. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
            elif self.player_one.chosen_gesture == "Scissors":
                if self.player_two.chosen_gesture == "Paper":
                    print(f"Scissors cuts Paper. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Lizard":
                    print(f"Scissors decapitates Lizard. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Rock":
                    print(f"Rock crushes Scissors. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Spock":
                    print(f"Spock smashes Scissors. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
            elif self.player_one.chosen_gesture == "Lizard":
                if self.player_two.chosen_gesture == "Spock":
                    print(f"Lizard poisons Spock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Paper":
                    print(f"Lizard eats Paper. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Rock":
                    print(f"Rock crushes Lizard. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Scissors":
                    print(f"Scissors decapitates Lizard. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
            elif self.player_one.chosen_gesture == "Spock":
                if self.player_two.chosen_gesture == "Scissors":
                    print(f"Spock smashes Scissors. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Rock":
                    print(f"Spock vaporizes Rock. {self.player_one.name} wins!")
                    self.player_one.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Lizard":
                    print(f"Lizard poisons Spock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
                elif self.player_two.chosen_gesture == "Paper":
                    print(f"Paper covers Rock. {self.player_two.name} wins!")
                    self.player_two.score += 1
                    print(f"{self.player_one.score} - {self.player_one.name}....{self.player_two.score} - {self.player_two.name}")
                    print()
                    print("*************************************************")
                    print()
