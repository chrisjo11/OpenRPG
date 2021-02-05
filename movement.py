# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#image = pygame.image.load(r'/Users/christopherjo/Documents/IntroToCompSci/Pygame/image/player.png')

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.image.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.image.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.image.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.image.move_ip(1, 0)

        # Keep player on the screen
        if self.image.left < 10:
            self.image.left = 10
        if self.image.right > SCREEN_WIDTH-10:
            self.image.right = SCREEN_WIDTH-10
        if self.image.top <= 10:
            self.image.top = 10
        if self.image.bottom >= SCREEN_HEIGHT-10:
            self.image.bottom = SCREEN_HEIGHT-10

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
    screen.fill((0, 200, 0))

    player.blit(image, (0, 0))

    # Update the display
    pygame.display.flip()