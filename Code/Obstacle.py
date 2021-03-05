# Imports
import pygame
from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obs_spritex, obs_spritey, filename):
        super(Obstacle, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.obs_sprite_image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.obs_sprite_image,(50,50))
        self.obs_sprite_height = 50
        self.obs_sprite_width = 50
        self.obs_spritex = obs_spritex
        self.obs_spritey = obs_spritey
        self.obs_hitbox = self.obs_sprite_image.get_rect()
    def getHitbox(self):
        return pygame.Rect(self.obs_spritex, self.obs_spritey, self.obs_sprite_width, self.obs_sprite_height)
    def inPortal(self, player):
        if player.spritex > 620 and player.spritey > 620:
            return True