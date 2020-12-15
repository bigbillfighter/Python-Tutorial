#settings

class Settings():
    def __init__(self):
        self.screen_length = 900
        self.screen_width = 400
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1

        self.bullet_speed = 0.5
        self.bullet_length = 15
        self.bullet_width = 3
        self.bullet_color = (120, 120, 120)
        self.bullets_allowed = 5