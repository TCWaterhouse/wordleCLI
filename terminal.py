class terminal:

    keys = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",],
            [" a", "s", "d", "f", "g", "h", "j", "k", "l  "],
            ["     z", "x", "c", "v", "b", "n", "m    "]
            ]

    def print_guess(word: str, colours: list):
        print(colours[0], word[0],
              colours[1], word[1],
              colours[2], word[2],
              colours[3], word[3],
              colours[4], word[4],
              terminal.bg.reset
            )
        
    def print_stats(player):
        pass
    
    def clear_line():
        print("\033[A                                                                                                     \033[A")

    def show_keys(wrong_letters: set):
        for line in terminal.keys:    
            key_line = ""
            for char in line:
                if char.strip() in wrong_letters:
                    key_line += (terminal.bg.black + terminal.fg.black + " " + char + " " + terminal.bg.reset)
                else:
                    key_line += (terminal.bg.lightgrey + " " + char + " " + terminal.bg.reset)
            print(key_line)

    def welcome_message(player, wordle):
        if player.last_played == wordle.todays_index:
            print(f"Hi {player.name} you've already tried today's puzzle")
            print("Would you like to see your stats? (y/n)")
            print("========================================================================")
            x = input()
            terminal.clear_line()
            if x.lower() == "y":
                terminal.print_stats(player)
                print("========================================================================")
            print("Come back tomorrow for a new puzzle!")
            quit()
        else:
            print(f"Welcome {player.name} to the daily world game!")
            print("Get 6 chances to guess a 5 letter word")
            print("Type 'help' to see which letters you've used but are not in today's word")
            print("========================================================================")

    def victory_message(guesses: int):
        print("========================================================================")
        if guesses == 1:
            print(f"Genius! You completed today's puzzle in {guesses} guess!")
        else:
            print(f"Congratulations! You completed today's puzzle in {guesses} guesses!")
        print("Come back tomorrow for a new puzzle!")

    def failure_message():
        print("========================================================================")
        print("You've ran out of guesses!")
        print("Come back tomorrow for another go")

    class fg:
        black = "\033[30m"
    
    class bg:
        reset = "\033[0m"
        green = "\033[42m"
        yellow = "\033[43m"
        black = "\033[40m"
        lightgrey = "\033[47m"
        darkgrey = "\033[100m"