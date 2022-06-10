import pygame
import random

import game_constants as gc

def handle_player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.rect.x > 0:
        player.rect.x -= gc.PLAYER_SPACESHIP_SPEED
    if  keys_pressed[pygame.K_RIGHT] and player.rect.x < gc.SCREEN_WIDTH - gc.PLAYER_IMAGE_WIDTH:
        player.rect.x += gc.PLAYER_SPACESHIP_SPEED


def handle_player_shot(player, bullet):
    #if keys_pressed[pygame.K_SPACE] and bullet.ready_for_shot == True:
    if bullet.ready_for_shot == True:
        bullet.rect.x = player.rect.x
        bullet.rect.y = player.rect.y - gc.PLAYER_IMAGE_HEIGHT
        bullet.ready_for_shot = False


def handle_bullet_movement(bullet):
    if bullet.ready_for_shot == False and bullet.rect.y > 0:
        bullet.rect.y -= gc.BULLET_SPEED
    else:
        bullet.ready_for_shot = True
        bullet.reset_position()


def handle_invader_movement(invader):
    # Direction handler
    if invader.movement_direction_right == True and invader.rect.x >= gc.SCREEN_WIDTH - gc.INVADER_IMAGE_WIDTH:
        invader.movement_direction_right = False
        invader.rect.y += gc.INVADER_IMAGE_HEIGHT
    if invader.movement_direction_right == False and invader.rect.x <= 0:
        invader.movement_direction_right = True
        invader.rect.y += gc.INVADER_IMAGE_HEIGHT
    # Movement increment
    if invader.movement_direction_right == True:
        invader.rect.x += gc.INVADER_SHIP_SPEED
    if invader.movement_direction_right == False:
        invader.rect.x -= gc.INVADER_SHIP_SPEED


def handle_collision_between_bullet_and_invader(bullet, invader):
    if bullet.collided_with(invader, gc.COLLISION_DISTANCE):
        bullet.ready_for_shot = True
        invader.rect.x = random.randint(0, gc.SCREEN_WIDTH - gc.INVADER_IMAGE_WIDTH)
        invader.rect.y = random.randint(0, gc.SCREEN_HEIGHT/3)
        invader.movement_direction_right = random.choice([True, False])
        return True
    else:
        return False


def is_game_over(invaders_list):
    flag = False
    for invader in invaders_list:
        if invader.rect.y >= gc.SCREEN_HEIGHT - gc.INVADER_IMAGE_HEIGHT:
            flag = True
            break
    return flag

