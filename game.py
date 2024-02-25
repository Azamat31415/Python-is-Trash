import pygame
from pygame.examples import aliens
import controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores
import sys

def main_menu(screen):
    background_image = pygame.image.load('images/space.jpg')

    while True:
        screen.blit(background_image, (0, 0))
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
    background_image = pygame.image.load('images/space.jpg')

    while True:
        screen.blit(background_image, (0, 0))

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
                pygame.quit()
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
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
    bg_color = (23, 13, 52)
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens, 3)
    stats = Stats()
    sc = Scores(screen, stats)

    main_menu(screen)

    while True:
        controls.events(screen, ship, bullets)
        if stats.run_game:
            ship.update_ship()
            controls.update(bg_color, screen, stats, sc, ship, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, ship, aliens, bullets)

run()
