import os
import pickle

from terminal import Terminal
from path import PATH


def load_player():
    if os.path.exists(f"{PATH}data/player.dat"):
        with open(f"{PATH}data/player.dat", "rb") as f:
            return pickle.load(f)
    else:
        print("Hey! It looks like this is your first time playing, what's your name?")
        name = input()
        print("\033[A                                                                                                     \033[A")
        print("\033[A                                                                                                     \033[A")
        return Player(name)
    
def save_player(player):
    with open(f"{PATH}data/player.dat", "wb") as f:
        pickle.dump(player, f)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.played = 0
        self.wins = 0
        self.current_streak = 0
        self.max_streak = 0
        self.guess_distribution = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        self.last_played = -1

