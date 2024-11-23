import random
import datetime


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
    todays_index = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).days
    todays_index -= 19420
    return todays_index

def test():
    i = get_todays_index()
    answers = get_answers()
    print(i % len(answers))

class Wordle():
    def __init__(self):
        self.answer_list = get_answer_list()
        self.supplement_list = get_supplemental_list()
        self.todays_index = get_todays_index()
        self.todays_word = self.answer_list[self.todays_index]
        self.guesses = 0


test()