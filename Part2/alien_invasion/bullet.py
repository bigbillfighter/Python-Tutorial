import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Administrate all the bullets'''

    def __init__(self, ai_settings, screen, ship):
        '''build an object at the location of the ship'''
        super(Bullet, self).__init__()
        self.screen = screen

        #build a bullet at the location of (0, 0) and set on the right location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        '''fly the bullets up'''
        #update the float location of the bullets
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw the bullets on the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)
