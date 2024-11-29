import os
import pickle

from terminal import terminal


def load_player():
    if os.path.exists("data/player.dat"):
        with open("data/player.dat", "rb") as f:
            return pickle.load(f)
    else:
        print("Hey! It looks like this is your first time playing, what's your name?")
        name = input()
        terminal.clear_line()
        terminal.clear_line()
        return Player(name)
    
def save_player(player):
    with open("data/player.dat", "wb") as f:
        pickle.dump(player, f)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.played = 0
        self.win_percentage = 0
        self.current_streak = 0
        self.max_streak = 0
        self.guess_distribution = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        self.last_played = -1

