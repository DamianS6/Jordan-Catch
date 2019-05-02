class Settings():
    """Defines settings for the game 'catch'."""

    def __init__(self):

        # Screen settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (200, 83, 65)

        self.speedup_scale = 1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.player_speed = 1.5
        self.ball_speed = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.player_speed *= self.speedup_scale
        self.ball_speed *= self.speedup_scale
