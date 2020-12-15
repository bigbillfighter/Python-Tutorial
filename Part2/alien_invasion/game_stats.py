#collect all the information of the game
class GameStats():
    '''follow all the information of the game'''
    def __init__(self, ai_settings):
        '''initialize all the information'''
        self.ai_settings = ai_settings
        self.reset_stats()

        #control if the game ends
        self.game_active = False

        self.max_score = 0

    def reset_stats(self):
        '''initialize all the information the may be changed
            on the procedure of running program
        '''

        self.ships_left = self.ai_settings.ship_lives
        self.score = 0
        self.level = 1





