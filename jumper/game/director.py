from display import Display
from hidden_word import Hidden_Word
from terminal_service import TerminalService

class Director:

    def __init__(self):
        self.word = Hidden_Word()
        self._is_playing = True
        self._display = Display()
        self._terminal_service = TerminalService()
        self._score = 0

    def game_start(self):
        while self._is_playing:
            self._get_inputs()
            # self._do_updates()
            # self._do_outputs()

    def _get_inputs(self):
        guess = input("Guess a letter?")
        self._display.word_reveal(self.word.get_word, guess)

    # def _do_updates(self):
    #     #
    #     #

    # def _do_outputs(self):

    #     if self._hidden_word.is_found():
    #         self._is_playing = False
    




#     def guess():
#         letter = input('Guess a letter A-Z')
        
#         pass
        
#     def update():
#         pass
        
#     def letter_val(self):
        
#         pass

director = Director()
director.game_start()