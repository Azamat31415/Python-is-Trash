import pygame
from pygame.examples import aliens

import controls
from ship import Ship
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Defender")
    icon = pygame.image.load('images/rocket.jpg')
    pygame.display.set_icon(icon)
    bg_color = (23, 13, 52)
    ship = Ship(screen)
    bullets = Group()
    alien = Group()
    controls.create_army(screen, alien)

    while True:
        controls.events(screen, ship, bullets)
        ship.update_ship()
        controls.update(bg_color, screen, ship, alien, bullets)
        controls.update_bullets(alien, bullets)
        controls.update_aliens(ship, alien)


run()
