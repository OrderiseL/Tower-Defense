import pygame
import math
from pygame.sprite import Sprite


# TODO:
#   1) load images
#   2) action when out of map
#

class Enemy:
    """
    Abstract class for all enemies.
    """
    images = []  # Class Variable

    def __init__(self):
        # Movement and animation
        self.path = [(18, 198), (110, 191), (161, 205), (198, 233), (266, 242),
                     (336, 241), (401, 242), (451, 241), (489, 222), (512, 170), (525, 137), (534, 92), (557, 57),
                     (607, 44), (658, 65), (685, 115), (704, 186), (731, 223), (778, 242), (844, 266), (875, 308),
                     (875, 366), (849, 404), (804, 429), (738, 437), (654, 430), (604, 431), (568, 472), (511, 477),
                     (449, 474), (382, 476), (293, 478), (117, 465),
                     (90, 435), (71, 368), (57, 329), (19, 294), (-40, 294)]

        self.animation_index = 0
        self.path_pos = 0
        self.img = None
        # set attributes
        self.width = 40
        self.height = 40
        self.vel = 3
        self.health = 1
        # Set position
        self.x = self.path[0][0]
        self.y = self.path[0][1] - self.height // 2
        self.add_y = 0  # Amount to add and keep even speed
        self.add_x = 0
        self._update_move_values()

    def draw(self, win):
        """
        Draws the enemy
        :param win: surface
        :return: None
        """
        # Set enemy
        self.move()
        self.img = self.images[self.animation_index]
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        win.blit(self.img, (int(self.x), int(self.y)))
        # Move to next frame
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
        Moves enemy from current checkpoint to next one
        :return:
        """
        self.x += self.add_x
        self.y += self.add_y
        # Check postion when moving right or left.
        if self.add_x > 0:
            # exceeded end position
            if (self.x + self.add_x) > self.path[self.path_pos][0]:
                self.path_pos += 1
                self._update_move_values()
        elif (self.x + self.add_x) < self.path[self.path_pos][0]:
            self.path_pos += 1
            self._update_move_values()

    def _update_move_values(self):
        """Calculates how to move according to angle"""
        print(self.add_x,self.add_y)
        start_p = self.path[self.path_pos]
        end_p = self.path[self.path_pos + 1]
        d = math.dist(start_p, end_p)
        xp = (start_p[0] * (d - self.vel) + end_p[0] * self.vel) / d
        yp = (start_p[1] * (d - self.vel) + end_p[1] * self.vel) / d
        self.add_x = xp-start_p[0]
        self.add_y = yp-start_p[1]

    def hit(self):
        """
        Removes scorp health and return if enemy has died
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return False
