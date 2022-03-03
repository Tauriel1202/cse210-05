
from game.casting.snake import Snake
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Player(Snake):
    def __init__(self, position: Point, color: Color):

        self._color_player = color
        self._position_player = position
        super().__init__()

    def _prepare_body(self):

        x = self._position_player.get_x()
        y = self._position_player.get_y()
        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color_player)
            self._segments.append(segment)
