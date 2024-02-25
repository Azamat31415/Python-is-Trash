import pygame
import random


class Alien(pygame.sprite.Sprite):
    """Class Alien"""

    def __init__(self, screen):
        """Initialization and setting the starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Alien output on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moving the aliens"""
        self.x += random.randint(-1, 1)
        self.y += random.uniform(0.1, 0.5) * 0.5
        self.rect.x = self.x
        self.rect.y = self.y
