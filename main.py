import pygame
import random

import game_constants as gc
from game_actions import (
    handle_collision_between_bullet_and_invader,
    handle_bullet_movement,
    handle_invader_movement,
    handle_player_movement,
    handle_player_shot,
    handle_collision_between_bullet_and_invader,
    is_game_over
    )
from game_objects import Player, Invader, Bullet

# Initialize pygame
pygame.init()

# Title and Icon
pygame.display.set_caption(gc.GAME_TITLE)
pygame.display.set_icon(pygame.image.load(gc.IMAGE_ICON))

SCREEN = pygame.display.set_mode((gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT))
PLAYER_SPACESHIP = pygame.image.load(gc.IMAGE_SPACESHIP)
INVADER_SHIP = pygame.image.load(gc.IMAGE_INVADER_SHIP)
BULLET = pygame.image.load(gc.IMAGE_BULLET)
FONT = pygame.font.Font('freesansbold.ttf', 32)


def draw_window(player, invaders_list, bullet, player_score):
    SCREEN.fill(gc.BLACK)

    score = FONT.render(gc.SCORE_MESSAGE + str(player_score), True, (255, 255, 255))
    SCREEN.blit(score, (10,10))

    SCREEN.blit(PLAYER_SPACESHIP,(player.rect.x, player.rect.y))

    for invader in invaders_list:
        SCREEN.blit(INVADER_SHIP, (invader.rect.x, invader.rect.y))

    if bullet.ready_for_shot == False:
        SCREEN.blit(BULLET, (bullet.rect.x, bullet.rect.y))

    pygame.display.update()


def main():
    player_rect = pygame.Rect(gc.SCREEN_WIDTH/2 - gc.PLAYER_IMAGE_WIDTH/2, gc.SCREEN_HEIGHT - gc.PLAYER_IMAGE_HEIGHT, gc.PLAYER_IMAGE_WIDTH, gc.PLAYER_IMAGE_HEIGHT)
    player = Player(player_rect, gc.PLAYER_SPACESHIP_SPEED)

    bullet_rect = pygame.Rect(gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT, gc.BULLET_IMAGE_WIDTH, gc.BULLET_IMAGE_HEIGHT)
    bullet = Bullet(bullet_rect, gc.BULLET_SPEED, True)

    invader_rect = pygame.Rect(0, 0, gc.INVADER_IMAGE_WIDTH, gc.INVADER_IMAGE_HEIGHT)
    invader = Invader(invader_rect, gc.INVADER_SHIP_SPEED, True)

    invaders_list = []
    invaders_list.append(invader)

    player_score = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(gc.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    handle_player_shot(player, bullet)

        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, player)
        handle_bullet_movement(bullet)

        for invader in invaders_list:
            handle_invader_movement(invader)
            collision = handle_collision_between_bullet_and_invader(bullet, invader)
            if collision:
                new_invader_rect = pygame.Rect(random.randint(0, gc.SCREEN_WIDTH - gc.INVADER_IMAGE_WIDTH), random.randint(0, gc.SCREEN_HEIGHT/3), gc.INVADER_IMAGE_WIDTH, gc.INVADER_IMAGE_HEIGHT)
                new_invader = Invader(new_invader_rect, gc.INVADER_SHIP_SPEED, True)
                invaders_list.append(new_invader)
                bullet.reset_position()
                player_score += 1

        if is_game_over(invaders_list):
            invaders_list.clear()
            print(gc.GAME_OVER_MESSAGE)

        draw_window(player, invaders_list, bullet, player_score)


if __name__ == "__main__":
    main()
