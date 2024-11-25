from wordle import *
from terminal import terminal

def main():
    game = Wordle()
    
    while game.guesses < 6:
        try:
            guess = input()
            terminal.clear_line()
            if game.error_flag:
                terminal.clear_line()
            if len(guess) != 5:
                raise Exception("Word is not 5 letters long!")
            if not guess.isalpha():
                raise Exception("Invalid characters used!")
            guess = guess.lower()
            colours = game.check_guess(guess)
            terminal.print_guess(guess, colours)
        except Exception as e:
            game.error_flag = True
            print(e)

if __name__ == "__main__":
    main()
