class Display:

    def __init__(self):
        pass

    def create_parachute():
        parachute = [ " ___ ","/___\ ", "\   /"," \ / "]
        for i in range(0 , 4):
            print(parachute[i])

    def create_guy():
        guy = ["  O  "," /|\ "," / \ ","     ","^^^^^"]
        for i in range((len(guy)-1)):
            print(guy[i])

    def word_reveal(word, guess):
        split_word = []
        for i in word:
            i.append(split_word)

        if guess == i:
            print(i)