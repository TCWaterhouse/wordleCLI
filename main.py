from wordle import *
from terminal import terminal

def main():
    game = Wordle()
    terminal.welcome_message()

    while game.guesses < 6:
        try:
            guess = input()
            terminal.clear_line()
            if game.help_flag:
                terminal.clear_line()
                terminal.clear_line()
                terminal.clear_line()
                game.help_flag = False
            if game.error_flag:
                terminal.clear_line()
                game.error_flag = False
            if guess.lower() == "help":
                terminal.show_keys(game.wrong_letters)
                game.help_flag = True
                continue
            if len(guess) != 5:
                raise Exception("Word is not 5 letters long!")
            if not guess.isalpha():
                raise Exception("Invalid characters used!")
            guess = guess.lower()
            colours, game_over = game.check_guess(guess)
            terminal.print_guess(guess, colours)
            if game_over:
                terminal.victory_message(game.guesses)
                quit()
        except Exception as e:
            game.error_flag = True
            print(e)

    terminal.failure_message()

if __name__ == "__main__":
    main()
