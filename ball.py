from random import randint

import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to represent a ball."""

    def __init__(self, settings, screen):
        """Initialize the ball and set its starting position."""
        self.screen = screen
        self.settings = settings

        super().__init__()
        ball = 'images/Basketball.jpeg'
        self.ball = pygame.image.load(ball)
        self.rect = self.ball.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the ball at the top of the screen.
        self.rect.left = randint(
            0, self.settings.screen_width - self.rect.width)
        self.top = float(self.screen_rect.top)

    def update(self):
        """Update the ball's position."""
        # Update the ball's top value, not the rect.
        self.top += self.settings.ball_speed

        # Update rect object from self.top.
        self.rect.top = self.top

    def blitme(self):
        self.screen.blit(self.ball, self.rect)
