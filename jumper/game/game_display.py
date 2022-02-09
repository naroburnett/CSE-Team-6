class game_display:

    def __init__(self):
        pass

    def parachute(director):
        parachute = [ " ___ ","/___\ ", "\   /"," \ / "]
        for i in range(director.score, 4):
            print(parachute[i])

    def guy():
        guy = ["  O  "," /|\ "," / \ ","     ","^^^^^"]
        for i in range((len(guy)-1)):
            print(guy[i])


game_display.parachute()
game_display.guy()