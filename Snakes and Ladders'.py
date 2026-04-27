import random

class game():
    def __init__(self):
        self.num_players = 0
        self.names = []
        self.player_pos = {}
        self.active_player_index = 0
        self.snakes = {16: 6, 48: 30, 64: 60, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.match_history = {}
        


    def start_game(self):
        while(self.num_players <= 1):
            try:
                self.num_players = int(input("Hello Player, Welcome to Snakes and Ladders, how many players will be playing today?(positive int > 1):"))

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

        while(not game_won):
            current_name = self.names[self.active_player_index]
            input(f"{current_name}'s turn, Press Enter to roll the dice\n")
            
            roll = random.randint(1, 6)
            print(f"{current_name} rolled a {roll}\n")
            
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

        if(winner in self.match_history): #add winner to match history
            self.match_history[winner] += 1
        else:
            self.match_history[winner] = 1
        