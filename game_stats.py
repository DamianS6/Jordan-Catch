class GameStats:
    """Store the statistics for the Jordan Catch."""

    def __init__(self):
        self.ball_limit = 3

        # Start Jordan Catch in an active state.
        self.game_active = False
