# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import *

from Player import Player
from Obstacle import Obstacle

# Initialize pygame
pygame.init()

# Instantiate player. Right now, this is just a rectangle.
player = Player()
obstacle = Obstacle(100, 100, 'Rock.png')
obstacleList = [obstacle]


SCREEN_WIDTH = player.SCREEN_WIDTH
SCREEN_HEIGHT = player.SCREEN_HEIGHT

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(obstacle)

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()



    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    player.checkHittingWall()
    playerHitbox = player.getHitbox()
    obstacleHitbox = obstacle.getHitbox()

    collide = playerHitbox.colliderect(obstacleHitbox)
    if collide:
        print("COLLISION")


    # Fill the screen with black
    screen.fill((50, 200, 50))

    # Draw the player on the screen
    screen.blit(player.image, (player.spritex, player.spritey))
    screen.blit(obstacle.image, (obstacle.obs_spritex, obstacle.obs_spritey))

    # Update the display
    pygame.display.flip()
    