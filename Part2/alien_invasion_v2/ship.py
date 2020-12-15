import pygame

class Ship():
    def __init__(self, screen, ai_settings):

        self.screen = screen
        self.ai_settings = ai_settings

        self.img = pygame.image.load('img/ship.bmp')
        self.rect = self.img.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        self.center = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom <self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed

        self.rect.centery = self.center

    def blitme(self):
        self.screen.blit(self.img, self.rect)