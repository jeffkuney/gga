# can you write me a python script that keeps score of a board game, and saves the inputs to json
# I'll help you create a Python script that keeps track of board game scores and saves them to a JSON file. Here's a simple implementation:

import json
from datetime import datetime

class ScoreKeeper:
    def __init__(self):
        self.scores = {}
        self.game_history = []
        self.filename = "game_scores.json"
        self.load_history()

    def load_history(self):
        try:
            with open(self.filename, 'r') as file:
                self.game_history = json.load(file)
        except FileNotFoundError:
            self.game_history = []

    def save_history(self):
        with open(self.filename, 'w') as file:
            json.dump(self.game_history, file, indent=4)

    def add_player(self, player_name):
        if player_name not in self.scores:
            self.scores[player_name] = 0
            print(f"Added player: {player_name}")
        else:
            print(f"Player {player_name} already exists!")

    def update_score(self, player_name, points):
        if player_name in self.scores:
            self.scores[player_name] += points
            print(f"{player_name}'s score is now {self.scores[player_name]}")
        else:
            print(f"Player {player_name} not found!")

    def show_scores(self):
        print("\nCurrent Scores:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")

    def end_game(self):
        game_record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "final_scores": self.scores.copy()
        }
        self.game_history.append(game_record)
        self.save_history()
        self.scores = {}
        print("\nGame ended and saved to history!")

def main():
    keeper = ScoreKeeper()
    
    while True:
        print("\n1. Add player")
        print("2. Update score")
        print("3. Show scores")
        print("4. End game")
        print("5. Show game history")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter player name: ")
            keeper.add_player(name)
        
        elif choice == "2":
            name = input("Enter player name: ")
            try:
                points = int(input("Enter points to add (negative for subtraction): "))
                keeper.update_score(name, points)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "3":
            keeper.show_scores()
        
        elif choice == "4":
            keeper.end_game()
        
        elif choice == "5":
            print("\nGame History:")
            for game in keeper.game_history:
                print(f"\nDate: {game['date']}")
                for player, score in game['final_scores'].items():
                    print(f"{player}: {score}")
        
        elif choice == "6":
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()