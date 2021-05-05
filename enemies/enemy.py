import pygame
from pygame.sprite import Sprite

class Enemy:
    """
    Abstract class for all enemies.
    """
    images = []  # Class Variable

    def __init__(self, x, y, width, height):
        # Set position
        self.x = x
        self.y = y
        # set attributes
        self.width = width
        self.height = height
        self.health = 1
        # Movement and animation
        self.path = []
        self.animation_index = 0
        self.img = None

    def draw(self, win):
        """
        Draws the enemy
        :param win: surface
        :return: None
        """
        self.move()
        self.img = self.images[self.animation_index]
        win.blit(self.img, (self.x, self.y))
        self.animation_index += 1
        if self.animation_index >= len(self.images):
            self.animation_index = 0

    def collide(self, x, y):
        """
        Return if position hit enemy
        :param x: int
        :param y: int
        :return:
        """
        if (self.width + self.x) >= x >= self.x and (self.height + self.y) >= y >= self.y:
            return True

    def move(self):
        """
        Moves enemy
        :return:
        """
        pass

    def hit(self):
        """
        Removes 1 health and return if enemy has died
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return False
