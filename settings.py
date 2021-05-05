import pygame

class Settings:
    """A class to store all Constants for modules"""

    def __init__(self):
        # Initialize screen settings
        self.scr_height = 1000
        self.scr_width = 700
        self.bg = pygame.image.load(r"assets\td-tilesets1-2\tower-defense-game-tilesets\PNG\game_background_2\game_background_2.png")