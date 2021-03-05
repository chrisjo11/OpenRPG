# Imports
import pygame
import Obstacle
import random
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
        self.surf = pygame.Surface((75, 25))
        self.sprite_image = pygame.image.load(spriteList["Down"])
        self.image = pygame.transform.scale(self.sprite_image,(40,50))
        self.sprite = spriteList["Down"]
        self.sprite_width = 40
        self.sprite_height = 50
        self.spritex = 100
        self.spritey = 100
        self.SCREEN_HEIGHT = 700
        self.SCREEN_WIDTH = 700
        
    def getHitbox(self): # Gets a hitbox for the player
        return pygame.Rect(self.spritex, self.spritey, self.sprite_width, self.sprite_height)

    def update(self, pressed_keys, isCollided): # Updates with every frame
        # Moves according to the key that is currently being pressed
        if pressed_keys[K_UP]:
            if not (pressed_keys[K_UP] and isCollided):
                self.spritey -= 0.5
            else:
                self.spritey += 30
        elif pressed_keys[K_DOWN]:
            if not (pressed_keys[K_DOWN] and isCollided):
                self.spritey += 0.5
            else:
                self.spritey -= 30
               
        elif pressed_keys[K_LEFT]:
            if not (pressed_keys[K_LEFT] and isCollided):
                self.spritex -= 0.5
            else:
                self.spritex += 30
        elif pressed_keys[K_RIGHT]:
            if not (pressed_keys[K_RIGHT] and isCollided):
                self.spritex += 0.5
            else:
                self.spritex -= 30

        # I
        if pressed_keys[K_UP]:
            self.sprite = spriteList["Up"]
        elif pressed_keys[K_DOWN]:
            self.sprite = spriteList["Down"]
        elif pressed_keys[K_LEFT]:
            self.sprite = spriteList["Left"]
        elif pressed_keys[K_RIGHT]:
            self.sprite = spriteList["Right"]

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