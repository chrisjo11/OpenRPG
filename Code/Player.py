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
        self.sprite_image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.sprite_image,(40,50))
        self.sprite_width = 40
        self.sprite_height = 50
        self.spritex = 0
        self.spritey = 0
        self.SCREEN_HEIGHT = 1000
        self.SCREEN_WIDTH = 1000
        self.lastKeyPressed = None
        
    def getHitbox(self):
        return pygame.Rect(self.spritex, self.spritey, self.sprite_width, self.sprite_height)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys, isCollided, lastkey):
        if pressed_keys[K_UP] and not(lastkey == "Up" and isCollided):
            self.spritey -= 0.3
            self.lastKeyPressed = "Up"
        elif pressed_keys[K_DOWN] and not(lastkey == "Down" and isCollided):
            self.spritey += 0.3
            self.lastKeyPressed = "Down"
        elif pressed_keys[K_LEFT] and not(lastkey == "Left" and isCollided):
            self.spritex -= 0.3
            self.lastKeyPressed = "Left"
        elif pressed_keys[K_RIGHT] and not(lastkey == "Right" and isCollided):
            self.spritex += 0.3
            self.lastKeyPressed = "Right"
    
    def checkHittingWall(self):
        if self.spritex < 0:
            self.spritex = 0
        if self.spritex + self.sprite_width > self.SCREEN_WIDTH:
            self.spritex = self.SCREEN_WIDTH - self.sprite_width
        if self.spritey <= 0:
            self.spritey = 0
        if self.spritey + self.sprite_height >= self.SCREEN_HEIGHT:
            self.spritey = self.SCREEN_HEIGHT - self.sprite_height