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
        self.sprite_image = pygame.image.load('sprite.gif')
        self.spritex = 10
        self.spritey = 10
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.spritey -= 1
        if pressed_keys[K_DOWN]:
            self.spritey += 1
        if pressed_keys[K_LEFT]:
            self.spritex -= 1
        if pressed_keys[K_RIGHT]:
            self.spritex += 1

        # Keep player on the screen
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > SCREEN_WIDTH:
        #     self.rect.right = SCREEN_WIDTH
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 225, 225))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.sprite_image, (player.spritex, player.spritey))

    # Update the display
    pygame.display.flip()