from deck import Deck

#Die == Deck
#dice == card
#roll == deal

'''
The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

'''

class Director:
    def __init__(self):
        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        card = Deck()
        self.card.append(card)

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.play_game()
            self.do_outputs()
    
    def get_inputs(self):
       draw_card = input('Do you want to continue playing? [y/n]:')
       self.is_playing = (draw_card == 'y')
    
    def play_game(self):
        if not self.is_playing:
            return
        hand = []
        if hand == '':
            hand.append(Deck.draw())
        else:
            pass

        print(f'The Card is : {hand}')
        hi_lo = input('Higher or Lower? [h/l]: ') 
        card = Deck.draw()
        if hi_lo == 'h':
            if card < hand:
                self.score += -75
                self.total_score += self.score

            if card > hand:
                self.score += 100
                self.total_score += self.score

        elif hi_lo == 'l':
            if card > hand:
                self.score += -75
                self.total_score += self.score
                
            if card < hand:
                self.score += 100
                self.total_score += self.score

        print(f'The card was: {card}')
        hand == card
    
    def do_outputs(self):
        if not self.is_playing:
            return
        
        print(f'Your score is: {self.total_score}')
        self.is_playing == (self.score > 0)





