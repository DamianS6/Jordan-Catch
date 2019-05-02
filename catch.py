import pygame

from settings import Settings
from game_stats import GameStats
from player import Player
from ball import Ball
from button import Button
import game_functions as gf


def run_game():
    """Initialize pygame, settings and screen object"""

    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Jordan Catch")

    button = Button(screen, "Play")

    player = Player(settings, screen)
    ball = Ball(settings, screen)
    stats = GameStats()

    # Start the main loop for the game.
    while True:

        gf.check_events(stats, player, button)

        if stats.game_active:
            player.update()
            gf.update_ball(ball, stats, settings, screen, player)

        gf.update_screen(settings, screen, stats, player, ball, button)


run_game()
