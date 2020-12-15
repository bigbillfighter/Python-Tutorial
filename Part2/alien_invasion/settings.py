class Settings():
    '''store all of the settings of the project "alen invision"'''
    def __init__(self):
        '''initialize all the settings of the game'''
        #screen settings
        self.screen_length = 1200
        self.screen_width = 700
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_lives = 3

        #bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        #alien setting
        self.fleet_drop_speed = 10

        #speed change
        self.speedup_scale = 1.1
        self.point_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''initialize the settings that will be changed when the game runs'''
        self.ship_speed = 3
        self.bullet_speed = 6
        self.alien_speed = 1
        #1 means right, -1 means left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        '''increase the speed'''
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.point_scale)

