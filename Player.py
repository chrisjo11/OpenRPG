# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import *

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.sprite_image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.sprite_image,(50,50))
        self.sprite_length = 50
        self.sprite_width = 50
        self.spritex = 10
        self.spritey = 10
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.spritey -= 0.3
        if pressed_keys[K_DOWN]:
            self.spritey += 0.3
        if pressed_keys[K_LEFT]:
            self.spritex -= 0.3
        if pressed_keys[K_RIGHT]:
            self.spritex += 0.3
        if self.spritex < 0:
            self.spritex = 0
        if self.spritex + 50 > SCREEN_WIDTH:
            self.spritex = SCREEN_WIDTH - self.sprite_length
        if self.spritey <= 0:
            self.spritey = 0
        if self.spritey + 50 >= SCREEN_HEIGHT:
            self.spritey = SCREEN_HEIGHT - self.sprite_width

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obs_spritex, obs_spritey):
        self.obs_sprite_image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.obs_sprite_image,(50,50))
        self.obs_sprite_length = 50
        self.obs_sprite_width = 50
        self.obs_spritex = obs_spritex
        self.obs_spritey = obs_spritey