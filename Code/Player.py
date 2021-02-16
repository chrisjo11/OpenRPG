# Import the pygame module
import pygame

import Obstacle

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import *

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.sprite_image = pygame.image.load('dot.png')
        self.image = pygame.transform.scale(self.sprite_image,(40,50))
        self.sprite_width = 50
        self.sprite_height = 50
        self.spritex = 0
        self.spritey = 0
        self.SCREEN_HEIGHT = 1000
        self.SCREEN_WIDTH = 1000
        self.hitbox = self.sprite_image.get_rect()
       

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
    
    def checkHittingWall(self):
        if self.spritex < 0:
            self.spritex = 0
        if self.spritex + self.sprite_width > self.SCREEN_WIDTH:
            self.spritex = self.SCREEN_WIDTH - self.sprite_width
        if self.spritey <= 0:
            self.spritey = 0
        if self.spritey + self.sprite_height >= self.SCREEN_HEIGHT:
            self.spritey = self.SCREEN_HEIGHT - self.sprite_height

    def is_collided_with(self, obstacle):
        return self.hitbox.colliderect(obstacle.obs_hitbox)