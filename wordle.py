import random
import datetime

from trie import Trie
from enum import Enum
from terminal import terminal


# Ensure that the words are always shuffled the same way
random.seed(69)

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


class Wordle:
    def __init__(self):
        answer_list = get_answer_list()
        self.todays_index = get_todays_index()
        self.todays_word = answer_list[self.todays_index % len(answer_list)]
        word_list = answer_list + get_supplemental_list()
        self.search_tree = build_search_tree(word_list)
        self.wrong_letters = set()
        self.guesses = 0 #TODO: Guesses should grab from a user file, so that it tracks play throughout the day.
        self.error_flag = False
        self.help_flag = False

    def check_guess(self, word: str):
        '''Checks to see if guess is valid. If it is, then it returns a list of the correct 5 ANSI colour escape codes'''
        if not self.search_tree.exists(word):
            raise ValueError("Word is not valid!")
        
        self.guesses += 1

        if word == self.todays_word:
            colours = [terminal.bg.green, terminal.bg.green, terminal.bg.green, terminal.bg.green, terminal.bg.green]
            return colours, True
        else:
            colours = []
            char_list = self.get_char_list()
            for i in range(5):
                if word[i] not in self.todays_word:
                    colours.append(terminal.bg.darkgrey)
                    self.wrong_letters.add(word[i])
                    continue
                elif word[i] not in char_list:
                    colours.append(terminal.bg.darkgrey)
                    continue
                elif word[i] == self.todays_word[i]:
                    colours.append(terminal.bg.green)
                    continue
                else:
                    colours.append(terminal.bg.yellow)
                    char_list.remove(word[i])
            return colours, False

    def get_char_list(self):
        char_list = []
        for char in self.todays_word:
            char_list.append(char)
        return char_list
