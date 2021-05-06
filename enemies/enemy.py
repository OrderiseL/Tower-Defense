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
        self.path = [(1, 192), (88, 193), (156, 200), (202, 237), (296, 240), (410, 240), (472, 228), (510, 190),
                     (522, 122), (549, 68), (621, 46), (673, 69), (698, 113), (706, 154), (724, 195), (759, 224),
                     (814, 230), (857, 262), (871, 301), (874, 348), (861, 396), (813, 418), (730, 423), (661, 423),
                     (611, 443), (567, 469), (507, 481), (405, 482), (257, 486), (154, 476), (112, 460), (86, 420),
                     (72, 358), (53, 319), (19, 290), (-40, 290)]
        # Movement and animation
        self.new_slope = False
        self.flipped = False
        self.animation_index = 0
        self.path_pos = 0
        self.img = None
        # set attributes
        self.width = 30
        self.height = 30
        self.vel = 3
        self.health = 1
        # to adjust y
        for i in range(len(self.path)):
            self.path[i] = list(self.path[i])
            self.path[i][1] -= self.height // 2
        # Set position
        self.x = self.path[0][0]
        self.y = self.path[0][1]
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
        self.img = pygame.transform.flip(self.img, self.flipped, False)

        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        win.blit(self.img, (int(self.x), int(self.y)))
        # Move to next frame
        self.animation_index += 1
        if self.animation_index >= len(self.images):
            self.animation_index = 0

    def move(self):
        """
        Moves enemy from current checkpoint to next one
        :return:
        """
        # Out of frame
        if (self.path_pos + 1) >= len(self.path):
            return
            # Move to next frame
        self.animation_index += 1
        # Reset animation
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.x += self.add_x
        self.y += self.add_y
        # Check postion when moving right or left.
        if self.add_x > 0:
            self.flipped = False
            # exceeded end position
            if (self.x + self.add_x) > self.path[self.path_pos + 1][0]:
                self.x = self.path[self.path_pos + 1][0]  # set at end position
                self.new_slope = True
        else:
            self.flipped = True  # moving left
            # exceeded end position
            if (self.x + self.add_x) < self.path[self.path_pos + 1][0]:
                self.x = self.path[self.path_pos + 1][0]  # set at end position
                self.new_slope = True
        # Check position moving Up or Down.
        if self.add_y > 0:  # Down
            # exceeded end position
            if (self.y + self.add_y) > self.path[self.path_pos + 1][1]:
                self.y = self.path[self.path_pos + 1][1]  # set at end position
                self.new_slope = True
        else:
            if (self.y + self.add_y) < self.path[self.path_pos + 1][1]:
                self.y = self.path[self.path_pos + 1][1]  # set at end position
                self.new_slope = True
        if self.new_slope:  # Calculate next x,y values
            self.path_pos += 1
            self._update_move_values()
            self.new_slope = False

    def _update_move_values(self):
        """Calculates how to move according to angle"""
        start_p = list((self.x, self.y))
        end_p = list(self.path[self.path_pos + 1])
        d = math.dist(start_p, end_p)
        xp = (start_p[0] * (d - self.vel) + end_p[0] * self.vel) / d
        yp = (start_p[1] * (d - self.vel) + end_p[1] * self.vel) / d
        self.add_x = xp - start_p[0]
        self.add_y = yp - start_p[1]

    def collide(self, x, y):
        """
        Return if position hit enemy
        :param x: int
        :param y: int
        :return:
        """
        if (self.width + self.x) >= x >= self.x and (self.height + self.y) >= y >= self.y:
            return True

    def hit(self):
        """
        Removes scorp health and return if enemy has died
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return False
