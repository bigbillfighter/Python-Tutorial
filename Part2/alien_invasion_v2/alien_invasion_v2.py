#Alien Invasion another version
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import  Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_length, ai_settings.screen_width))
    pygame.display.set_caption("Alian Invasion V2")

    ship = Ship(screen, ai_settings)

    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, ai_settings)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()