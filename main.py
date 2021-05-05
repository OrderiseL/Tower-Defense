import os
import sys
import pygame
from enemies.scorpion import Scorpion
from settings import Settings


# noinspection PyMethodMayBeStatic
class Game:
    def __init__(self):
        pygame.init()
        self.active = True
        # initalize main window settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.scr_width, self.settings.scr_height))
        # Objects
        self.enemies = [Scorpion()]
        self.towers = []
        # Player resources
        self.lives = 10
        self.money = 100

    def run(self):
        """Function to run game"""
        clock = pygame.time.Clock()

        while self.active:
            clock.tick(60)  # Limit framerate
            self._update_screen()
            self._check_events()

        pygame.quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exit")
                self.active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def _update_screen(self):
        # Load background
        self.screen.blit(self.settings.bg, (0, 0))
        for enemy in self.enemies:
            enemy.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()
