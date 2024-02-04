import pygame
import sys
from bullet import Bullet
from alien import Alien

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


def update(bg_color, screen, ship, aliens, bullets):
    """Screen update"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(aliens, bullets):
    """Updating the bullets position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_aliens(ship, aliens):
    """Updating the aliens position"""
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        print('!!!')


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
