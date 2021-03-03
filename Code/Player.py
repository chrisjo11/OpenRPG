# Import the pygame module
import pygame

import Obstacle

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import *

# Makes a list of filenames

spriteList = {
    "Down": "playerDown.png",
    "Up" : "playerUp.png",
    "Left": "playerLeft.png",
    "Right": "playerRight.png",
}

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self): # Initiate player class
        super(Player, self).__init__()
        self.lastKeyPressed = None
        self.surf = pygame.Surface((75, 25))
        self.sprite_image = pygame.image.load(spriteList["Down"])
        self.image = pygame.transform.scale(self.sprite_image,(40,50))
        self.sprite_width = 40
        self.sprite_height = 50
        self.spritex = 0
        self.spritey = 0
        self.SCREEN_HEIGHT = 700
        self.SCREEN_WIDTH = 700
        
    def getHitbox(self):
        return pygame.Rect(self.spritex, self.spritey, self.sprite_width, self.sprite_height)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys, isCollided, lastkey):
        if pressed_keys[K_UP]:
            if not (lastkey == "Up" and isCollided):
                self.spritey -= 0.5
                self.lastKeyPressed = "Up"
            else:
                self.spritey += 5
                self.lastKeyPressed = "Up"
        elif pressed_keys[K_DOWN]:
            if not (lastkey == "Down" and isCollided):
                self.spritey += 0.5
                self.lastKeyPressed = "Down"
            else:
                self.spritey -= 5
                self.lastKeyPressed = "Down"
        elif pressed_keys[K_LEFT]:
            if not (lastkey == "Left" and isCollided):
                self.spritex -= 0.5
                self.lastKeyPressed = "Left"
            else:
                self.spritex += 5
                self.lastKeyPressed = "Left"
        elif pressed_keys[K_RIGHT]:
            if not (lastkey == "Right" and isCollided):
                self.spritex += 0.5
                self.lastKeyPressed = "Right"
            else:
                self.spritex -= 5
                self.lastKeyPressed = "Right"

        if self.lastKeyPressed == "Up":
            self.sprite = spriteList["Up"]
        elif self.lastKeyPressed == "Down":
            self.sprite = spriteList["Down"]
        elif self.lastKeyPressed == "Left":
            self.sprite = spriteList["Left"]
        elif self.lastKeyPressed == "Right":
            self.sprite = spriteList["Right"]
        else:
            self.sprite = spriteList["Down"]

        self.sprite_image = pygame.image.load(self.sprite)
        self.image = pygame.transform.scale(self.sprite_image,(40,50))
    
    def checkHittingWall(self):
        if self.spritex < 0:
            self.spritex = 0
        if self.spritex + self.sprite_width > self.SCREEN_WIDTH:
            self.spritex = self.SCREEN_WIDTH - self.sprite_width
        if self.spritey <= 0:
            self.spritey = 0
        if self.spritey + self.sprite_height >= self.SCREEN_HEIGHT:
            self.spritey = self.SCREEN_HEIGHT - self.sprite_height