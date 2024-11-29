class Terminal:
    def __init__(self, player, wordle):
        self.player = player
        self.wordle = wordle

    keys = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",],
            [" a", "s", "d", "f", "g", "h", "j", "k", "l  "],
            ["     z", "x", "c", "v", "b", "n", "m    "]
            ]

    def print_guess(self, word: str, colours: list):
        print(colours[0], word[0],
              colours[1], word[1],
              colours[2], word[2],
              colours[3], word[3],
              colours[4], word[4],
              self.bg.reset
            )
        
    def print_stats(self):
        print(f"Played: {self.player.played}, Win%: {(self.player.wins/self.player.played*100):.0f}, Current Streak: {self.player.current_streak}, Max Streak: {self.player.max_streak}")
        print("========================================================================")
        for i in range(1, 7):
            self.print_guess_distribution_bar(self.player.guess_distribution[i], self.player.wins, prefix = f"[{i}]", length = 50)
    
    def print_guess_distribution_bar(self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\n"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    def check_stats(self):    
        print("Would you like to see your stats? (y/n)")
        print("========================================================================")
        x = input()
        self.clear_line()
        self.clear_line()
        if x.lower() == "y":
            self.print_stats()
            print("========================================================================")

    def clear_line(self):
        print("\033[A                                                                                                     \033[A")

    def show_keys(self):
        for line in self.keys:    
            key_line = ""
            for char in line:
                if char.strip() in self.wordle.wrong_letters:
                    key_line += (self.bg.black + self.fg.black + " " + char + " " + self.bg.reset)
                else:
                    key_line += (self.bg.lightgrey + " " + char + " " + self.bg.reset)
            print(key_line)

    def welcome_message(self):
        if self.player.last_played == self.wordle.todays_index:
            print(f"Hi {self.player.name} you've already tried today's puzzle")
            self.check_stats()
            print("Come back tomorrow for a new puzzle!")
            quit()
        else:
            print(f"Welcome {self.player.name} to the daily world game!")
            print("Get 6 chances to guess a 5 letter word")
            print("Type 'help' to see which letters you've used but are not in today's word")
            print("========================================================================")

    def victory_message(self):
        print("========================================================================")
        if self.wordle.guesses == 1:
            print(f"Genius! You completed today's puzzle in {self.wordle.guesses} guess!")
        else:
            print(f"Congratulations! You completed today's puzzle in {self.wordle.guesses} guesses!")
        # Update stats of player
        self.player.played += 1
        self.player.wins += 1
        self.player.current_streak += 1
        if self.player.current_streak > self.player.max_streak:
            self.player.max_streak = self.player.current_streak
        self.player.guess_distribution[self.wordle.guesses] += 1
        self.player.last_played = self.wordle.todays_index
        self.check_stats()
        print("Come back tomorrow for a new puzzle!")

    def failure_message(self):
        print("========================================================================")
        print("You've ran out of guesses!")
        # Update stats of player
        self.player.played += 1
        self.player.current_streak = 0
        self.player.last_played = self.wordle.todays_index
        self.check_stats()
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