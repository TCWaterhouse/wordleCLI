from wordle import *
from terminal import terminal

def main():
    game = Wordle()
    
    print("Welcome to the daily world game!")
    print("Get 6 chances to guess a 5 letter word")

    while game.guesses < 6:
        try:
            guess = input()
            terminal.clear_line()
            if guess.lower() == "help":
                terminal.show_keys(game.wrong_letters)
                game.help_flag = True
                continue
            if game.error_flag:
                terminal.clear_line()
                game.error_flag = False
            if len(guess) != 5:
                raise Exception("Word is not 5 letters long!")
            if not guess.isalpha():
                raise Exception("Invalid characters used!")
            guess = guess.lower()
            colours, game_over = game.check_guess(guess)
            terminal.print_guess(guess, colours)
            if game_over:
                if game.guesses == 1:
                    print(f"Genius! You completed today's puzzle in {game.guesses} guess!")
                else:
                    print(f"Congratulations! You completed today's puzzle in {game.guesses} guesses!")
                print("Come back tomorrow for a new puzzle!")
                quit()
        except Exception as e:
            game.error_flag = True
            print(e)

    print("You've ran out of guesses!")
    print("Come back tomorrow for another go")

if __name__ == "__main__":
    main()
