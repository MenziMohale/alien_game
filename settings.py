import  pygame
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
        self.ship_speed = 2.5
        self.bg_image = pygame.image.load('Images/bg_image (4).jpeg')

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (88, 255, 88)
        self.bullet_allowed = 10
