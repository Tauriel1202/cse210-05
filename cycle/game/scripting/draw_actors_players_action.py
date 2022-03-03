from game.scripting.draw_actors_action import DrawActorsAction


class DrawActorPlayersAction(DrawActorsAction):
    def __init__(self, video_service):
        super().__init__(video_service)

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")

        #snake = cast.get_first_actor("snakes")
        #segments = snake.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        for player in cast.get_actors('snakes'):
            self._video_service.draw_actors(player.get_segments())
            # print(f"{player.get_position().get_x()}:{player.get_position().get_y()}")

        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
