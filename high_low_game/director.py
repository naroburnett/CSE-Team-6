from high_low_game.deck import Deck

#Die == Deck
#dice == card
#roll == deal

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deal (List[deal]): A list of deal instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.is_playing = True
        self.score = 300
        self.total_score = 300

        deck = Deck()
        self.card.append(deck)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        i = 0
        while self.is_playing:
            if i == 0:  
                start = self.game_start()
                self.get_inputs()
                self.do_updates()
                self.do_outputs()
                i += 1
            else:
                start = self.game_start()
                self.get_inputs()
                self.do_updates()
                self.do_outputs()
                

    def game_start(deck):
        start = deck.deal()
        return start
        

    def get_inputs(self):
        """Ask the user if they want to continue playing.

        Args:
            self (Director): An instance of Director.
        """
        continue_play = input("Play again? [y/n]")
        self.is_playing = (continue_play == "y")

        
    def do_updates(self, start):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        high_low = input('Higher or lower? [h/l]')
        
        
        deck = self.deck
        deck.deal() # Get card from deck
        if high_low == "h":
            deck.deal ,

        self.score += deck.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the deal and the score. Also asks the player if they want to deal again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.deck)):
            deck = self.deck[i]
            values += f"{deal.value} "

        print(f"Next card was: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)