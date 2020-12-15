import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        '''initialize teh location of the ship'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get the square around the image
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #put every new ship born at the bottom of the surface
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #store float location coordinates
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #moving flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def center_ship(self):
        '''put the ship on the center of screen'''
        self.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centery = self.rect.centery


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed

        #update centerx based on center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        '''draw the ship'''
        self.screen.blit(self.image, self.rect)