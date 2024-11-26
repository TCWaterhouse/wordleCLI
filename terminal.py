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
    
    def clear_line():
        print("\033[A                                       \033[A")

    def show_keys(wrong_letters: set):
        for line in terminal.keys:    
            key_line = ""
            for char in line:
                if char in wrong_letters:
                    key_line += (terminal.bg.black + terminal.fg.black + " " + char + " " + terminal.bg.reset)
                else:
                    key_line += (terminal.bg.lightgrey + " " + char + " " + terminal.bg.reset)
            print(key_line)

    class fg:
        black = "\033[30m"
    
    class bg:
        reset = "\033[0m"
        green = "\033[42m"
        yellow = "\033[43m"
        black = "\033[40m"
        lightgrey = "\033[47m"
        darkgrey = "\033[100m"