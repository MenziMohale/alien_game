import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class represents alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set the position"""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('Images/alien ufo.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien horizontal position
        self.x = float(self.rect.x)

