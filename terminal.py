class terminal:
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

    class bg:
        reset = "\033[0m"
        green = "\033[42m"
        yellow = "\033[43m"
        lightgrey = "\033[47m"
        darkgrey = "\033[100m"