import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """the class as one alien"""
    def  __init__(self, ai_settings, screen):
        """Initialize the original location"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and set the rect attribute
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        #every alien appears at the center of the screen top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the exact locations of aliens
        self.x = float(self.rect.x)

    def if_on_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        '''aliens move right'''
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)