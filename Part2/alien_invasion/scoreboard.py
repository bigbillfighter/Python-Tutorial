import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    '''class to display the score'''
    def __init__(self, ai_settings, screen, stats):
        '''initialize the attributes associated with displaying scores'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #set the font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        #set the initial score image
        self.prep_score()
        self.prep_max_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''change the font to image'''
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #put the score on the top right cornor of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_max_score(self):
        """change max score to image"""
        max_score = int(round(self.stats.max_score, -1))
        max_score_str = "{:,}".format(max_score)
        self.max_score_image = self.font.render(max_score_str, True, self.text_color, self.ai_settings.bg_color)

        #put the maximum score on the top of center
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.centerx = self.screen_rect.centerx
        self.max_score_rect.top = self.screen_rect.top

    def prep_level(self):
        '''change the level of the ship'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        #put level beneath the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''show how many ships left'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

