import random

class game():
    def __init__(self):        
        self.num_players = 0
        self.names = []
        self.player_pos = {}
        self.active_player_index = 0
        self.snakes = {16: 6, 48: 30, 64: 60, 93: 73, 95: 75, 98: 78}
        self.ladders = {2: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.match_history = {}



    def start_game(self):
        while(self.num_players <= 1):
            try:
                self.num_players = int(input("\nHello Player, Welcome to Snakes and Ladders, how many players will be playing today?(positive int > 1):"))

                if(self.num_players <= 0):
                    print("Invalid input, please enter a positive integer")

            except Exception: #not an integer
                print("Invalid input, please enter a positive integer")

        count = len(self.names)

        while(count < self.num_players):
            name = input(f"Enter player #{count + 1}'s name: ")

            if(name in self.names): #edge case
                print("This name is already taken, try again\n")

            else:
                self.names.append(name)
                self.player_pos[name] = 1
                count += 1

        print("--------------------------------------------------------------\n\nLet's Begin\n")

        self.play()



    def play(self):
        winner = ""
        game_won = False
        choice = ""

        while(not game_won):
            current_name = self.names[self.active_player_index]
            choice = input(f"{current_name}'s turn, press Enter (any input) to roll the dice or type Quit to exit to main menu: ")
            
            if (choice == "Quit"):
                game_won = True
                print() #spacer for text

            else:
                roll = random.randint(1, 6)
                print(f"\n{current_name} rolled a {roll}\n")
                
                old_pos = self.player_pos[current_name]
                new_pos = old_pos + roll
                
                if(new_pos > 100):
                    print(f"You need exactly 100 to win, You stay at square {old_pos}\n")
                    new_pos = old_pos

                if(new_pos in self.ladders):
                    print(f"You landed on a Ladder, it took you from square {new_pos} to {self.ladders[new_pos]}\n")
                    new_pos = self.ladders[new_pos]
                    
                if(new_pos in self.snakes):
                    print(f"You landed on a Snake, it took you from square {new_pos} to {self.snakes[new_pos]}\n")
                    new_pos = self.snakes[new_pos]
                
                self.player_pos[current_name] = new_pos #update position after role
                print(f"{current_name} is now at square {new_pos}\n")
                
                if(new_pos == 100): #win con
                    print(f"Congradulations {current_name}, you win!\n")
                    winner = current_name
                    game_won = True

                else:
                    self.active_player_index = (self.active_player_index + 1) % self.num_players #moves to the next player in the order
                    print("--------------------------------------------------------------\n")

        if(winner): #add winner to match history, skips if game was quit
            if(winner in self.match_history): 
                self.match_history[winner] += 1
            else:
                self.match_history[winner] = 1
        
        self.end_game()



    def end_game(self):
        choice = ""
        print("--------------------------------------------------------------\n")

        while (choice not in ["1", "2", "3", "4"]):
            print("1. Play again (Same Players)")
            print("2. New Game (Wipe everything but match history)")
            print("3. View Match History")
            print("4. Quit Game")
            choice = input("Select an option(1-4): ")

            if (choice == "1"):
                self.reset(False)
                self.start_game()

            elif (choice == "2"):
                self.reset(True)
                self.start_game()

            elif (choice == "3"):
                self.view_match_history()

            elif (choice == "4"):
                print("\nThank you for playing, have a great day")
                #effectively quits since no code runs

            else:
                print("\nInvalid selection, try again\n")



    def reset(self, full_reset):
        self.active_player_index = 0

        if (full_reset):
            self.num_players = 0
            self.names = []
            self.player_pos = {}

        else:
            idx = 0

            #just resets the position of current players (new game with same players)
            while (idx < len(self.names)):
                self.player_pos[self.names[idx]] = 1
                idx += 1
    


    def view_match_history(self):
        print("\n--------- MATCH HISTORY ---------")

        if (not self.match_history):
            print("No games recorded yet")

        else:
            history_keys = list(self.match_history.keys())
            idx = 0

            while (idx < len(history_keys)):
                name = history_keys[idx]
                print(f"{name}: {self.match_history[name]} wins")
                idx += 1

        print("---------------------------------\n")

        self.end_game()


my_game = game()
my_game.start_game()
