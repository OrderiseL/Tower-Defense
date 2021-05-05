import pygame
import math
from pygame.sprite import Sprite


class Enemy:
    """
    Abstract class for all enemies.
    """
    images = []  # Class Variable

    def __init__(self, width, height):
        # Set position
        self.x = 0
        self.y = 0
        self.add_y = 0  # Amount to add and keep even speed
        self.add_x = 0
        # set attributes
        self.width = width
        self.height = height
        self.vel = 3
        self.health = 1
        # Movement and animation
        self.path = [(22, 192),
                     (82, 194), (138, 194), (183, 222), (224, 242), (267, 242), (360, 242), (441, 239), (499, 212),
                     (518, 150), (536, 92), (581, 56), (649, 60), (682, 101), (702, 159), (712, 203), (742, 228),
                     (799, 244), (845, 268), (872, 316), (868, 366), (844, 405), (784, 432), (693, 434), (618, 440),
                     (570, 473), (500, 481), (434, 478), (359, 476), (156, 473), (110, 450), (81, 424), (71, 374),
                     (38, 305), (9, 286), (-40, 286)]
        self.animation_index = 0
        self.path_pos = 0
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
        Moves enemy from current checkpoint to next one
        :return:
        """
        # When
        # Moving right.
        self.x += self.add_x
        self.y += self.add_y
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
        start_p = self.path[self.path_pos]
        end_p = self.path[self.path_pos + 1]
        d = math.dist(start_p, end_p)
        xp = int((start_p[0] * (d - self.vel) + end_p[0] * self.vel) / d)
        yp = int((start_p[1] * (d - self.vel) + end_p[1] * self.vel) / d)
        self.add_x = abs(start_p[0] - xp)
        self.add_y = abs(start_p[1] - yp)

    def hit(self):
        """
        Removes 1 health and return if enemy has died
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return False
