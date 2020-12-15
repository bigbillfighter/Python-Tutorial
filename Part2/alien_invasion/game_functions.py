import sys
import pygame
from bullet import Bullet
from time import sleep
from alien import Alien

def get_aliens_num_columns(ai_settings, alien_width):
    available_space_x = ai_settings.screen_length - 2 * alien_width
    number_columns = int(available_space_x / (2 * alien_width))
    return number_columns

def get_aliens_num_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_width - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_columns, alien_rows):
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2 * alien_columns * alien.rect.width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_rows

    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    '''create the aliens group'''

    #calculate the number that the aliens can be built
    alien = Alien(ai_settings, screen)
    number_columns = get_aliens_num_columns(ai_settings, alien.rect.width)
    number_rows = get_aliens_num_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_columns):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    '''do actions when aliens touch the edges'''
    for alien in aliens.sprites():
        if alien.if_on_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''change the direction of fleet'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def fire_bullet(ai_settings, screen, ship, bullets):
    '''if wasn't up to the ceiling, build a new bullet'''
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown(event, ai_settings, screen, stats, ship, bullets):
    '''response keys down'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_r and not stats.game_active:
        stats.game_active = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, ship):
    '''response keys up'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_play_botton(ai_settings, screen, stats, sb, play_buttton, ship, aliens, bullets, mouse_x, mouse_y):
    '''when player click the botton, the game starts'''
    button_click = play_buttton.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        #let mouse invisible
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #reset the scoreboard
        sb.prep_score()
        sb.prep_max_score()
        sb.prep_level()


    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    '''response the keyboard and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_botton(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''renew the images on the screen to new images'''
    #redraw the screen on every loop
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #show the score
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()
    #only display the most recent screen
    pygame.display.flip()

def check_max_score(stats, sb):
    """check if a new maximum coce was born"""
    if stats.score > stats.max_score:
        stats.max_score = stats.score
        sb.prep_max_score()


def check_alien_bullet_collision(ai_settings, screen, stats, sb, ship, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_max_score(stats, sb)

    if len(aliens)==0:
        #if all the aliens are distroyed, we generate a new group of aliens
        bullets.empty()
        #speedup the speed
        ai_settings.increase_speed()

        #level up
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''update the locations of bullets'''
    #update the locations of bullets
    bullets.update()
    # delete the vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_alien_bullet_collision(ai_settings, screen, stats, sb, ship, bullets, aliens)


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """reponce the ship that crashed by the aliens"""
    #reduce the lives of ship
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #reset the scoreboard
        sb.prep_ships()

        #empty the aliens list and the bullet list
        aliens.empty()
        bullets.empty()

        #create a new list of aliens and put the ship on the center of bottom
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            '''process like ship was crashed'''
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    '''update all the locations of aliens'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #check if there is any collision on any alien and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


