import pygame
import sys
from bullet import Bullet
from alien import Alien
import time

def events(screen, ship, bullets):
    """Event processing"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Right
            if event.key == pygame.K_RIGHT:
                ship.mright = True
            # Left
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
            # Shot
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # Right
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            # Left
            elif event.key == pygame.K_LEFT:
                ship.mleft = False


def update(bg_color, screen, stats, sc, ship, aliens, bullets):
    """Screen update"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, aliens, bullets):
    """Updating the bullets position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 1 * len(aliens)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_ships()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)

def ship_kill(stats, screen, sc, ship, aliens, bullets):
    """The clash of the army and the ship"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sc.image_ships()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        ship.create_ship()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_aliens(stats, screen, sc, ship, aliens, bullets):
    """Updating the aliens position"""
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_kill(stats, screen, sc,  ship, aliens, bullets)
    aliens_check(stats, screen, sc, ship, aliens, bullets)

def aliens_check(stats, screen, sc, ship, aliens, bullets):
    """Checking the passage of the army to the end of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_kill(stats, screen, sc, ship, aliens, bullets)


def create_army(screen, aliens):
    """Create army of aliens"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)

def check_high_score(stats, sc):
    """Checking the high scores"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
