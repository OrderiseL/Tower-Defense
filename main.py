import os
import sys
import pygame
from settings import Settings


class Game:
    def __init__(self):
        pygame.init()
        # initalize main window settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.height, self.width))
        # Objects
        self.enemies = []
        self.towers = []
        # Player resources
        self.lives = 10
        self.money = 100

    def run(self):
        """Function to run game"""
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)  # Limit framerate
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    run = False
            self._update_screen()

        pygame.quit()

    def _update_screen(self):
        # Load background
        self.screen.blit(self.settings.bg, (0, 0))

        pygame.display.update()
