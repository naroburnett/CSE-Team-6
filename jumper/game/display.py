class Display:

    def __init__(self):
        self.parachute_display = [" ___ ","/___\ ", "\   /"," \ / "]
        self.guy_display = ["  O  "," /|\ "," / \ ","     ","^^^^^"]
        self.word_display = ["_","_","_","_","_"]
        self.guessed_letters_display = []

    def create_parachute(self,score):
        parachute = [ " ___ ","/___\ ", "\   /"," \ / "]
        parachute_list = []
        for i in range(score , 4):
            parachute_list.append(parachute[i])
        self.parachute_display = parachute_list

    def create_guy(self):
        guy = ["  O  "," /|\ "," / \ ","     ","^^^^^"]
        guy_list = []
        for i in range((len(guy)-1)):
            guy_list.append(guy[i])
        self.guy_display = guy_list

    def create_word_banner(self, word, guess):
        if word.find(guess) != -1:
            for i in range(5):
                if guess == word[i-1]:
                    self.word_display[i-1] = guess
                i += 1
            
        else: 
            print("try again")
            self.guessed_letters_display.append(f'{guess}')
            

    def display_results(self):
        print(*self.word_display)
        print(*self.parachute_display, sep="\n")
        print(*self.guy_display, sep="\n")
        print('Guessed Letters:')
        print(*self.guessed_letters_display, sep=", ")
        print()

# display = Display()
# score = 4
# guess = 's'
# word = 'Adult'
# display.create_word_banner(word, guess)
# display.create_parachute(score)
# display.create_guy()
# display.display_results()