import random
import datetime

from trie import Trie


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
    '''Returns the supplemental list'''
    supplemental_list = []
    with open("data/en_5words_supplemental.txt", "r") as p:
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
    search_tree = Trie()
    for word in word_list:
        search_tree.add(word)
    return search_tree


class Wordle():
    def __init__(self):
        answer_list = get_answer_list()
        self.todays_index = get_todays_index()
        self.todays_word = answer_list[self.todays_index % len(answer_list)]
        word_list = answer_list.append(get_supplemental_list())
        self.search_tree = build_search_tree(word_list)
        #FIXME: Guesses should grab from a user file, so that it tracks play throughout the day.
        self.guesses = 0

    #TODO: break into multiple funcs. check if correct. check if valid. check which chars are correct. 
    # What am i returning? :/
    def check_guess(word: str):
        pass