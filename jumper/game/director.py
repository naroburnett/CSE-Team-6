# import word
# import game.game_display
from game_display import game_display

class director:

    def __init__(self):
        self.score = 5
        pass

    

    def game_start(self):
        game_display.guy(self)
        game_display.parachute(self)
        



#     def guess():
#         letter = input('Guess a letter A-Z')
        
#         pass
        
#     def update():
#         pass
        
#     def letter_val(self):
        
#         pass

# director.game_start()