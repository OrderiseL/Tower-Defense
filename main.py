import pygame
from enemies.enemy_types import *
from settings import Settings
from towers.tower_types import *
import random
import time


class Game:
    def __init__(self):
        pygame.init()
        self.active = True
        self.timer = time.time()
        # initalize main window settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.scr_width, self.settings.scr_height))
        # Objects
        self.enemies = []
        self.towers = [LongArcher(300, 300), ShortArcher(800,300)]
        # Player resources
        self.lives = 10
        self.money = 100

    def run(self):
        """Function to run game"""
        clock = pygame.time.Clock()

        while self.active:
            clock.tick(60)  # Limit framerate
            # spawn new enemies:
            if (time.time() - self.timer) > 0.5:
                self.timer = time.time()
                self.enemies.append(random.choice([Scorpion(), Clubber(), Wizard()]))
            self._update_screen()
            self._check_events()
            # Check enemies:
            for e in self.enemies:
                # Enemies passed end.
                if e.out:
                    self.enemies.remove(e)
            # Check towers:
            if self.enemies:
                for tw in self.towers:
                    tw.attack(self.enemies)
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
        # load objects
        for enemy in self.enemies:
            enemy.draw(self.screen)

        for tower in self.towers:
            tower.draw(self.screen)

        pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()
