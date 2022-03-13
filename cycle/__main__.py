import constants

from game.casting.cast import Cast
# from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
# x 900
# y 600

def main():
    #creates player 1
    player_1 = Cycle()
    pos_x = 300
    pos_y = 300
    color_body = constants.YELLOW
    color_head = constants.GREEN

    player_1._prepare_body(pos_x, pos_y , color_body, color_head)

    #creates platyer 2
    player_2 = Cycle()
    pos_x = 600
    pos_y = 600
    color_body = constants.RED
    color_head = constants.BLUE

    player_2._prepare_body(pos_x, pos_y , color_body, color_head)



    # create the cast
    cast = Cast()
    # cast.add_actor("foods", Food())
    cast.add_actor("cycles", player_1)
    cast.add_actor("cycles2", player_2)
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()