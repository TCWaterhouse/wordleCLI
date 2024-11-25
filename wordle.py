import random
import datetime

from trie import Trie
from enum import Enum


# Ensure that the words are always shuffled the same way
random.seed(69)

Colour = Enum("Colour", ["GREEN", "YELLOW", "GREY"])

def get_answer_list() -> list[str]:
    '''Returns the answer list after doing some basic QA and shuffling'''
    answers_list = []
    with open("data/en_5words_answers.txt", "r") as p:
        for line in p:
            answers_list.append(line.strip())
    answers_list = [word.lower() for word in answers_list if len(word) == 5 and word.isalpha()]
    random.shuffle(answers_list)
    return answers_list

def get_supplemental_list() -> list[str]:
    '''Returns the supplement list after doing some basic QA'''
    supplemental_list = []
    with open("data/en_5words_supplement.txt", "r") as p:
        for line in p:
            supplemental_list.append(line.strip())
    supplemental_list = [word.lower() for word in supplemental_list if len(word) == 5 and word.isalpha()]
    return supplemental_list

def get_todays_index() -> int:
    '''Returns the index for today'''
    todays_index = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).days
    todays_index -= 19420
    return todays_index

def build_search_tree(word_list: list[str]) -> Trie:
    '''Returns a search tree (Trie Object) to be used for quickly checking if guesses are valid'''
    search_tree = Trie()
    for word in word_list:
        search_tree.add(word)
    return search_tree


class Wordle():
    def __init__(self):
        answer_list = get_answer_list()
        self.todays_index = get_todays_index()
        self.todays_word = answer_list[self.todays_index % len(answer_list)]
        word_list = answer_list + get_supplemental_list()
        self.search_tree = build_search_tree(word_list)
        self.guesses = 0 #TODO: Guesses should grab from a user file, so that it tracks play throughout the day.

    def check_guess(self, word: str) -> list[Colour]:
        if not self.search_tree.exists(word):
            raise ValueError("Word is not valid!")
        
        if word == self.todays_word:
            return [Colour.GREEN, Colour.GREEN, Colour.GREEN, Colour.GREEN, Colour.GREEN]
        else:
            guess = []
            char_list = self.get_char_list()
            for i in range(5):
                print(char_list)
                if word[i] == self.todays_word[i]:
                    guess.append(Colour.GREEN)
                    continue
                elif word[i] in char_list:
                    guess.append(Colour.YELLOW)
                    char_list.remove(word[i])
                    continue
                else:
                    guess.append(Colour.GREY)
            return guess

    def get_char_list(self):
        char_list = []
        for char in self.todays_word:
            char_list.append(char)
        return char_list


def test():
    wordle = Wordle()
    print(wordle.todays_word)
    word = "llama"
    print(word)
    result = wordle.check_guess(word)
    print(result)

test()