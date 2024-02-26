import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen):
        """Ship's initialization"""
        super(Ship,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom - 20
        self.mright = False
        self.mleft = False

    def output(self):
        """Ship's draw"""
        self.screen.blit(self.image, self.rect)

    def update_ship(self):
        """Updating the ship position"""
        move_speed = 1.4
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += move_speed
        if self.mleft and self.rect.left > 0:
            self.center -= move_speed

        self.rect.centerx = self.center

    def create_ship(self):
        """Placing the ship in the center"""
        self.center = self.screen_rect.centerx

