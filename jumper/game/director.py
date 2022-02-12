from game.display import Display
from game.hidden_word import Hidden_Word
from game.terminal_service import TerminalService

class Director:

    def __init__(self):
        self.hidden_word = Hidden_Word()
        self._is_playing = True
        self._display = Display()
        self._terminal_service = TerminalService()
        self._score = 0
        self.guess = ''
    
    def calculate_guess(self):
        self._display.create_word_banner(self.hidden_word.secret_word, self.guess)
        self._display.create_parachute(self._score)
        self._display.create_guy()

    def results(self):
         self._display.display_results()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.starting_info()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
    

    def starting_info(self):
        self.results()

    def _get_inputs(self):
        self.guess = input("Guess a Letter?: ").lower()

    def _do_updates(self):
        self.calculate_guess()

        

    def _do_outputs(self):
        self.results()

        self._score = len(self._display.guessed_letters_display)
        if self._score == 5:
           self._is_playing = False
           print('GAME OVER')
           print(f'The word was: {self.hidden_word.secret_word}.')

        elif "_" not in self._display.word_display:
            self._is_playing = False
            print('You WON!')
