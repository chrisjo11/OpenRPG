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

stage1 = open("stageOne.txt")
stage1List = []

for line in stage1:
    lineStrip = line.strip()
    stage1List.append(lineStrip)

SCREEN_WIDTH = player.SCREEN_WIDTH
SCREEN_HEIGHT = player.SCREEN_HEIGHT

obstacleRock = Obstacle(100, 100, 'rock.png')
obstacleBush = Obstacle(200, 200, 'tree.png')
obstacleBush2 = Obstacle(300, 200, 'bush.png')

obstacleList = [obstacleRock, obstacleBush, obstacleBush2]

i = 0
for obs in stage1List:
    obstacleList.append(Obstacle(i, 0, 'tree.png'))
    i += 50

portalObject = Obstacle(SCREEN_WIDTH - 60, SCREEN_HEIGHT - 60, 'portal.png')

print(obstacleList)

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
score = 0

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
    bg = pygame.image.load('grass.png')
    bg_scaled = pygame.transform.scale(bg,(700,700))
    screen.blit(bg_scaled,(0,0))

    for item in obstacleList:
        screen.blit(item.image, (item.obs_spritex, item.obs_spritey))
        collide = playerHitbox.colliderect(item.getHitbox())
        player.update(pressed_keys, collide)

    if portalObject.inPortal(player):
        score += 1
        player.spritex = 100
        player.spritey = 100
    
    # set the pygame window name
    pygame.display.set_caption('Open RPG')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Score: " + str(score), True, (255, 255, 255), (0, 150, 50))
    screen.blit(text, (10, 660))
 
    # Draw the player on the screen
    screen.blit(player.image, (player.spritex, player.spritey))

    screen.blit(portalObject.image, (portalObject.obs_spritex, portalObject.obs_spritey))

    # Update the display
    pygame.display.flip()