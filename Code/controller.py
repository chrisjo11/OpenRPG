# Imports
import pygame
import random
from pygame.locals import *
from Player import Player
from Obstacle import Obstacle

# Initialize pygame
pygame.init()

# Instantiate player. Also add obstacles
player = Player()
obstacleRock = Obstacle(100, 100, 'rock.png')
obstacleBush = Obstacle(100, 100, 'bush.png')
obstacleList = [obstacleRock, obstacleBush]


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
for item in obstacleList:
    all_sprites.add(item)

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
    player.checkHittingWall()
    playerHitbox = player.getHitbox()

    #create a background
    bg = pygame.image.load('background.jpeg')
    bg_scaled = pygame.transform.scale(bg,(700,700))
    screen.blit(bg_scaled,(0,0))

    for item in obstacleList:
        collide = playerHitbox.colliderect(item.getHitbox())
        screen.blit(item.image, (item.obs_spritex, item.obs_spritey))
    player.update(pressed_keys, collide, player.lastKeyPressed)

    # Draw the player on the screen
    screen.blit(player.image, (player.spritex, player.spritey))

    # Update the display
    pygame.display.flip()