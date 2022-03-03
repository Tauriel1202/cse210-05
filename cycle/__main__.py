import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.snake import Snake
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
from game.casting.player import Player
from game.scripting.draw_actors_players_action import DrawActorPlayersAction


def main():

    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())

    player1 = Player(Point(200, int(constants.MAX_Y/2)), constants.RED)
    player1.turn_head(Point(0, -constants.CELL_SIZE))

    player2 = Player(Point(400, int(constants.MAX_Y/2)), constants.GREEN)
    player2.turn_head(Point(0, constants.CELL_SIZE))

    cast.add_actor("snakes", player1)
    cast.add_actor("snakes", player2)
    cast.add_actor("scores", Score())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorPlayersAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
