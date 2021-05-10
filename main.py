from typing import List, Union
import pygame
from enemies.enemy_types import *
import settings
from towers.tower_types import *
import random
import time

pygame.init()
pygame.font.init()

heart = pygame.transform.scale(pygame.image.load("used_assets\heart.png"), (36, 36))
star_img = pygame.image.load("used_assets\star.png")
font = pygame.font.SysFont("comicsans", 60)


class Game:

    def __init__(self):
        self.active = True
        self.timer = time.time()
        # initalize main window settings
        self.screen = pygame.display.set_mode((settings.scr_width, settings.scr_height))
        # Objects
        self.enemies = []
        self.attack_towers = [LongArcher(300, 300), ShortArcher(800, 300)]
        self.support_towers = [SpeedTower(300, 400)]
        self.selected_tower = None
        # Player resources
        self.lives = 10
        self.money = 100

    def run(self):
        """Function to run game"""
        clock = pygame.time.Clock()

        while self.active:
            clock.tick(60)  # Limit framerate
            # spawn new enemies:
            if (time.time() - self.timer) > 1:
                self.timer = time.time()
                self.enemies.append(random.choice([Scorpion(), Clubber(), Wizard()]))
            self._update_screen()
            self._check_events()
            # Check enemies:
            for e in self.enemies:
                # Enemies passed end.
                if e.out:
                    self.lives -= 1
                    self.enemies.remove(e)
                elif e.dead:  # killed
                    self.enemies.remove(e)
            if self.lives == 0:
                self.active = False
                break
            # Check attack_towers:
            if self.enemies:
                for tw in self.attack_towers:
                    tw.attack(self.enemies)
            # Support towers:
            for tower in self.support_towers:
                tower.support(self.attack_towers)
        pygame.quit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exit")
                self.active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_down_events()

    def _mouse_down_events(self):
        """
        Handles mouse press events
        :return: None
        """
        pos = pygame.mouse.get_pos()
        # Selected tower:
        if self.selected_tower and self.selected_tower.menu.is_clicked(pos[0], pos[1]):
            pass
        else:
            for tower in (self.support_towers + self.attack_towers):
                if tower.click(pos[0], pos[1]):
                    self.selected_tower = tower

    def _update_screen(self):
        # Draw background
        self.screen.blit(settings.bg, (0, 0))
        # Draw objects
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for tower in self.attack_towers:
            tower.draw(self.screen)
        for tower in self.support_towers:
            tower.draw(self.screen)
        # Draw lives
        txt = font.render(str(self.lives), 1, (255, 255, 255))
        self.screen.blit(heart, (self.screen.get_width() - heart.get_width() - 10, 10))
        self.screen.blit(txt, (self.screen.get_width() - heart.get_width() - txt.get_width() - 10, 10))
        pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()
