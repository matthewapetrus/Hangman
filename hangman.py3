class Hangman:

    def __init__(self, word):
        self.word = word
        self.word_list = [char for char in self.word]
        self.display_list = ['__'] * len(self.word_list)
        self.guessed_letters = []
        print(f"Guess: {self.display_list}")
        self.guesses = 0

    def display_man(self):
        str_man = "     |       "
        str_man += "\n     |       "
        for guess in range(self.guesses):
            if guess+1 == 1:
                str_man += "\n     0       "
            if guess+1 == 2:
                str_man += "\n    /"
            if guess+1 == 3:
                str_man += ":"
            if guess+1 == 4:
                str_man += '\\'
            if guess+1 == 5:
                str_man += "\n     :      "
            if guess+1 == 6:
                str_man += "\n    / "
            if guess+1 == 7:
                str_man += "\\"

        print(str_man)

    def guess_letter(self, letter):
        if letter in self.word_list:
            print('-----------------')
            print("Correct Guess!")
            self.display_man()
            
            indexes = [index for index, value in enumerate(self.word_list) if value == letter]

            for i in range(len(self.display_list)):
                if i in indexes:
                    self.display_list[i] = letter

            if ''.join(self.display_list) == self.word:
                print("You Win! :)")
                print(f"{self.display_list}")
            else:
                print(f"Guess: {self.display_list}")
                self.guessed_letters.append(letter)
            print(f"Guessed Letters: {self.guessed_letters}")
            print('-----------------')
        else:
            print('-----------------')
            print('Incorrect Guess')
            self.guesses += 1
            self.display_man()
            print(f"Guess: {self.display_list}")
            self.guessed_letters.append(letter)
            print(f"Guessed Letters: {self.guessed_letters}")
            
            if self.guesses == 7:
                print("You Lose :(")
            print('-----------------')


game = Hangman('hello')
game.guess_letter('l')
game.guess_letter('r')
game.guess_letter('t')
game.guess_letter('y')
game.guess_letter('m')
game.guess_letter('n')
game.guess_letter('p')
game.guess_letter('b')