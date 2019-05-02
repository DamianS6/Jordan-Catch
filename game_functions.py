import sys
from time import sleep

import pygame


def check_keydown_events(event, player):
    """Respond to key presses."""
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        player.move_right = True
    elif event.key == pygame.K_LEFT:
        player.move_left = True


def check_keyup_events(event, player):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        player.move_right = False
    elif event.key == pygame.K_LEFT:
        player.move_left = False


def check_events(stats, player, button):
    """Watch for keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, button, mouse_x, mouse_y)


def check_play_button(stats, button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    if button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        pygame.mouse.set_visible(False)


def update_screen(settings, screen, stats, player, ball, button):
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)

    if not stats.game_active:
        button.draw_button()
    if stats.game_active:
        ball.blitme()
    player.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def ball_missed(settings, stats, screen, ball):
    # Check for the missed ball, reset the speed and decrease ball limit.
    if stats.ball_limit > 0:
        if ball.rect.bottom >= settings.screen_height:
            ball.__init__(settings, screen)
            settings.initialize_dynamic_settings()
            stats.ball_limit -= 1
            sleep(0.5)
    else:
        stats.game_active = False


def update_ball(ball, stats, settings, screen, player):
    """Update ball's position and replace old one with a new one."""
    # Update ball's position.
    ball.update()
    # Check for a ball catched by player.
    # If it happens, create new, faster ball
    # and slightly increase player's movement speed.
    if pygame.sprite.collide_rect(player, ball):
        if settings.player_speed <= 9:
            settings.increase_speed()
        ball.__init__(settings, screen)
    else:
        ball_missed(settings, stats, screen, ball)
