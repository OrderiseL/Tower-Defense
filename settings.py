import pygame


class Settings:
    """A class to store all Constants for modules"""

    def __init__(self):
        # Initialize screen settings
        self.scr_width = 1000
        self.scr_height = 600
        self.bg = pygame.image.load(r"used_assets\game_background_2.png")
        self.bg = pygame.transform.scale(self.bg, (self.scr_width, self.scr_height))
        # Enemy settings
