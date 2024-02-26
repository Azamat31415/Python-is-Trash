import pygame.font
from ship import Ship
from pygame.sprite import Group



class Scores():
    """Game information output"""
    def __init__(self, screen, stats):
        """Initialization scores"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (87, 155, 203)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_ships()

    def image_score(self):
        """Converting the invoice text"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (23, 13, 52))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """Converting the high score"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (23, 13, 52))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_ships(self):
        """The number of lives"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen)
            ship.image = pygame.transform.scale(ship.image, (75 / 2, 85 / 2))
            ship.rect.x = 15 + (ship_number * ship.rect.width)
            ship.rect.y = 20
            self.ships.add(ship)

    def show_score(self):
        """Score output on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)
