import math
import sys

import pygame
from pygame.sprite import Group

import controls
from scores import Scores
from ship import Ship
from stats import Stats


def main_menu(screen):
    bg = pygame.image.load('images/space.jpg')

    while True:
        screen.blit(bg, (0, 0))
        font = pygame.font.Font(None, 64)
        text = font.render("Space Defender", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
        screen.blit(text, text_rect)

        start_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50, 200, 50)
        pygame.draw.rect(screen, (0, 255, 0), start_button)
        font = pygame.font.Font(None, 36)
        text = font.render("Start game", True, (0, 0, 0))
        text_rect = text.get_rect(center=start_button.center)
        screen.blit(text, text_rect)

        quit_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 120, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)
        text = font.render("Quit", True, (0, 0, 0))
        text_rect = text.get_rect(center=quit_button.center)
        screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def game_over_screen(screen):
    bg = pygame.image.load('images/space.jpg')

    while True:
        screen.blit(bg, (0, 0))

        font = pygame.font.Font(None, 64)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
        screen.blit(text, text_rect)

        restart_button = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() // 2 + 50, 300, 50)
        pygame.draw.rect(screen, (0, 255, 0), restart_button)
        font = pygame.font.Font(None, 36)
        text = font.render("Restart Game", True, (0, 0, 0))
        text_rect = text.get_rect(center=restart_button.center)
        screen.blit(text, text_rect)

        quit_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 150, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)
        text = font.render("Quit", True, (0, 0, 0))
        text_rect = text.get_rect(center=quit_button.center)
        screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"
                elif quit_button.collidepoint(event.pos):
                    return "quit"

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Defender")
    icon = pygame.image.load('images/rocket.jpg')
    pygame.mixer.music.load('sounds/kanye.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    pygame.display.set_icon(icon)
    bg = pygame.image.load('images/bg.png')
    bg_height = bg.get_height()
    bgs = math.ceil(bg_height / 700)
    scroll = 0
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens, 1)
    stats = Stats()
    sc = Scores(screen, stats)

    main_menu(screen)

    while True:
        controls.events(screen, ship, bullets, stats)
        if stats.run_game:
            for i in range(0, bgs):
                screen.blit(bg, (0, -1 * i * bg_height + scroll))

            scroll += 2

            if abs(scroll) > bg_height:
                scroll = 0

            ship.update_ship()
            controls.update(screen, sc, ship, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, ship, aliens, bullets)
        else:
            response = game_over_screen(screen)

            if response == "quit":
                pygame.quit()
                sys.exit()
            if response == "restart":
                stats.run_game = True
                stats.reset_stats()
                stats.ships_left += 1

run()
