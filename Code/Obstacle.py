import py

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obs_spritex, obs_spritey):
        self.obs_sprite_image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.obs_sprite_image,(50,50))
        self.obs_sprite_length = 50
        self.obs_sprite_width = 50
        self.obs_spritex = obs_spritex
        self.obs_spritey = obs_spritey