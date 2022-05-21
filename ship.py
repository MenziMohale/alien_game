import pygame

class Ship:
    """ Class creates a ship for the game and manage the ship"""

    def __init__(self, ai_game):
        """Initilizes the ship adn starting point"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship3.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position (x axis).
        self.x = float(self.rect.x)

        # Movement of the ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag"""
        # Prevents image from passing before running ship speed code from settings module
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)
