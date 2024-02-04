import pygame
from pygame.examples import aliens
import controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores


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
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, ship, bullets)
        if stats.run_game:
            ship.update_ship()
            controls.update(bg_color, screen, stats, sc, ship, alien, bullets)
            controls.update_bullets(screen, stats, sc, alien, bullets)
            controls.update_aliens(stats, screen, sc,  ship, alien, bullets)


run()
