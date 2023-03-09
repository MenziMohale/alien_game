import pygame

class Settings():
    """Stores all setting for the game"""

    def __init__(self):
        """Initilizes the setting for the game"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 820
        self.bg_color = (0, 0, 0)
        #self.image = pygame.image.load('Images/bmp test 2.png')
        # Ship speed settings
        self.ship_limit = 3
        self.bg_image = pygame.image.load('Images/bg_image (4).jpeg')

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (88, 255, 88)
        self.bullet_allowed = 10

        # Alien settings
        self.alien_fleet_drop = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.alien_fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly an alien point value increases
        self.score_scale = 1.5

        self.initilize_dynamic_settings()

    def initilize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increases the speed settings and alien points"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

