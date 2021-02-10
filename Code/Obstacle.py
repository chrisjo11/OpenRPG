# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import *
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obs_spritex, obs_spritey):
        super(Obstacle, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.obs_sprite_image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.obs_sprite_image,(50,50))
        self.obs_sprite_length = 50
        self.obs_sprite_width = 50
        self.obs_spritex = obs_spritex
        self.obs_spritey = obs_spritey