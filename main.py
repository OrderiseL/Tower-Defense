import os
import sys
import pygame


class Game:
    def __init__(self):
        # initalize main window settings
        self.height = 1000
        self.width = 700
        self.win = pygame.display.set_mode((self.height, self.width))
        # Objects
        self.enemies = []
        self.towers = []
        # Player resources
        self.lives = 10
        self.money = 100

    def run(self):
        """Function to run game"""
        run = True
        while run:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    run = False

        pygame.quit()
