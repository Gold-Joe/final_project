import random

class game():
    def __init__(self):
        self.num_players = 0
        self.names = []
        self.player_pos = {}
        self.snakes = {16: 6, 48: 30, 64: 60, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        


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
        