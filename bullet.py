import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, ship):
        """Create the bullet in ship position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 228, 19, 19
        self.speed = 4.5
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

