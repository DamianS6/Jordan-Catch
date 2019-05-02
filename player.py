import pygame


class Player():
    """A class to represent a player."""

    def __init__(self, settings, screen):
        """Initialize the player and set its starting position."""
        self.screen = screen
        self.settings = settings

        # Load the player's image and get it's rect.
        player = 'images/michael_jordan.png'
        self.player = pygame.image.load(player)
        self.rect = self.player.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the player at the bottom center of the screen.
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags
        self.move_right = False
        self.move_left = False

    def update(self):
        """Update the player's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.move_right and self.rect.right <= self.settings.screen_width:
            self.center += self.settings.player_speed
        if self.move_left and self.rect.left >= 0:
            self.center -= self.settings.player_speed

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.player, self.rect)
