import random

class Dice():
    def __init__(self):
        self.die1 = None
        self.die2 = None
    
    def roll1(self,die1):
        roll = random.randint(1,6)
        return roll

    def roll2(self,die2):
        roll = random.randint(1,6)
        return roll

    def total(self,roll1,roll2):
        total = roll1 + roll2
        return total
