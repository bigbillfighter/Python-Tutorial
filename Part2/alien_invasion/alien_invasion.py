import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
#from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    '''initialize the game and draw a window'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_length, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    #build the button
    play_button = Button(ai_settings, screen, "Play")

    #set the lives of ship
    stats = GameStats(ai_settings)
    #create the score board
    sb = Scoreboard(ai_settings, screen, stats)

    #build a ship
    ship = Ship(screen, ai_settings)

    #build a goup to administrate all the bullets
    bullets = Group()

    #build aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #the main loop of the game
    while True:
        #monitor the keyboard and mouse
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        #draw all the elements
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()



