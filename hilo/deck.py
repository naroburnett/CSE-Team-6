import random


class Deck:
    def __init__(self):
        #creates an instance of a card
        self.card = 0

    def draw(self):
        #draws a random card from deck
        self.value = random.randint(1, 13)