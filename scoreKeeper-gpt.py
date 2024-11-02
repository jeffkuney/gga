# can you write me a python script that keeps score of a board game, and saves the inputs to json
# Here's a Python script that manages and saves the scores of a board game. It tracks the players' scores, keeps an updated tally, and saves each player's score to a JSON file.

import json

class BoardGameScoreKeeper:
    def __init__(self, player_names):
        self.scores = {player: 0 for player in player_names}
        self.history = []

    def update_score(self, player, points):
        if player in self.scores:
            self.scores[player] += points
            self.history.append({"player": player, "points": points, "total_score": self.scores[player]})
            print(f"Updated {player}'s score by {points} points. Total score: {self.scores[player]}")
        else:
            print(f"Player {player} not found!")

    def save_scores(self, filename="game_scores.json"):
        data = {
            "scores": self.scores,
            "history": self.history
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Scores saved to {filename}")

    def load_scores(self, filename="game_scores.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.scores = data["scores"]
                self.history = data["history"]
            print(f"Scores loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found. Starting a new game.")

# Example usage
players = ["Alice", "Bob", "Charlie"]
score_keeper = BoardGameScoreKeeper(players)

# Update scores
score_keeper.update_score("Alice", 10)
score_keeper.update_score("Bob", 5)
score_keeper.update_score("Charlie", 15)

# Save scores to JSON
score_keeper.save_scores()

# Load scores from JSON (if restarting the game)
score_keeper.load_scores()