import pygame
import math
import settings
import A_STAR_pathfinding as asp
from loader import node_grid


# TODO: Have some powerup spawn on map

class Enemy:
    """
    Abstract class for all enemies.
    """

    def __init__(self):
        # set attributes
        self.worth = 50
        self.width = settings.wiz_width
        self.height = settings.wiz_height
        self.speed = 3
        self.max_health = 3
        self.health = self.max_health
        self.main_path = asp.a_star_search((26, 0), (43, 0), node_grid)
        self.main_path_pos = 0
        self.curr_path = self.main_path
        # Movement and animation
        self.new_slope = False
        self.flipped = False
        self.animation_index = 0
        self.path_pos = 0
        self.images = []  # Class Variable
        self.img = None
        self.out = False
        self.dead = False
        # Set position
        self.row, self.col = self.curr_path[0]
        self.x, self.y = asp.get_pos(self.curr_path[0])
        self.x = -self.width
        self.add_y = 0  # Amount to add and keep even speed
        self.add_x = 0
        self._update_move_values()
        # Powerup:
        self.targeting = None  # Contains target powerup

    def draw(self, screen):
        """
        Draws the enemy
        :param screen: surface
        :return: None
        """
        if self.out:
            return
        # Draw enemy
        self.img = self.images[int(self.animation_index)]
        self.img = pygame.transform.flip(self.img, self.flipped, False)
        screen.blit(self.img, (int(self.x), int(self.y)))
        # Draw Health bar
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        """
        Draws health bar above enemy
        :param screen: Surface
        :return: None
        """
        length = self.width - 5
        h_increment = length / self.max_health
        curr_health = int(self.health * h_increment)
        pygame.draw.rect(screen, (80, 80, 80), (self.x, self.y - 10, length, 5), 0)
        pygame.draw.rect(screen, (0, 200, 0), (self.x, self.y - 10, curr_health, 5), 0)

    def move(self):
        """
        Moves enemy from current checkpoint to next one
        :return: None
        """
        # Increase to next frame
        self.animation_index += self.speed / 5
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.x += self.add_x
        self.y += self.add_y
        if (self.path_pos + 1) >= len(self.curr_path):
            return
        # Check postion when moving right or left.
        end = self.curr_path[self.path_pos + 1]
        e_x, e_y = asp.get_pos(end)
        if self.add_x > 0:
            self.flipped = False
            # exceeded end position
            if (self.x + self.add_x) > e_x:
                # self.x = e_x  # set at end position
                self.new_slope = True
        else:
            self.flipped = True  # moving left
            # exceeded end position
            if (self.x + self.add_x) < e_x:
                # self.x = e_x  # set at end position
                self.new_slope = True
        # Check position moving Up or Down.
        if self.add_y > 0:  # Down
            # exceeded end position
            if (self.y + self.add_y) > e_y:
                # self.y = e_y  # set at end position
                self.new_slope = True
        else:
            if (self.y + self.add_y) < e_y:
                # self.y = e_y  # set at end position
                self.new_slope = True
        if self.new_slope:  # Calculate next x,y values
            self.path_pos += 1
            # Out of frame
            if (self.path_pos + 1) >= len(self.curr_path):
                self.out = True
                return
            self._update_move_values()
            self.new_slope = False

    def _update_move_values(self):
        """Calculates how to move according to angle"""
        start_p = list((self.x, self.y))
        end_p = list(self.curr_path[self.path_pos + 1])
        end_p = asp.get_pos(end_p)
        d = math.dist(start_p, end_p)
        xp = (start_p[0] * (d - self.speed) + end_p[0] * self.speed) / d
        yp = (start_p[1] * (d - self.speed) + end_p[1] * self.speed) / d
        self.add_x = xp - start_p[0]
        self.add_y = yp - start_p[1]

    def collide(self, x, y):
        """
        Return if position hit enemy
        :param x: int
        :param y: int
        :return:
        """
        if (self.width + self.x) >= x >= self.x \
                and (self.height + self.y) >= y >= self.y:
            return True
        return False

    def hit(self, damage):
        """
        Removes health and return if enemy has died
        :return: Bool
        """
        self.health -= damage
        if self.health <= 0:
            self.dead = True
            if self.targeting:
                self.targeting.is_targeted = False
            return self.worth
        return 0

    def move_to_powerup(self, powerup):
        """
        set next path to power up.
        :param powerup: Powerup
        :return:
        """
        powerup.is_targeted = True
        self.targeting = powerup
        dest = tuple(powerup.rect.center)
        dest = asp.get_reverse_pos(dest)
        if self.x < 0:
            self.x = 0
        src = asp.get_reverse_pos((int(self.x), int(self.y)))
        shortest_path = asp.a_star_search(src, dest, node_grid)
        self.curr_path = shortest_path
        self.main_path_pos = self.path_pos
        self.path_pos = 0

    def find_main_pathpos(self):
        end = self.main_path[self.path_pos + 1]
        e_x, e_y = asp.get_pos(end)
        while True:
            # Check postion when moving right or left.
            if self.add_x > 0:
                self.flipped = False
                # exceeded end position
                if (self.x + self.add_x) > e_x:
                    self.new_slope = True
            else:
                self.flipped = True  # moving left
                # exceeded end position
                if (self.x + self.add_x) < e_x:
                    self.new_slope = True
            # Check position moving Up or Down.
            if self.add_y > 0:  # Down
                # exceeded end position
                if (self.y + self.add_y) > e_y:
                    self.new_slope = True
            else:
                if (self.y + self.add_y) <e_y:
                    self.new_slope = True
            if self.new_slope:  # Calculate next x,y values
                self.main_path_pos += 1
                # Out of frame
                self.new_slope = False
                if (self.main_path_pos + 1) >= len(self.main_path):
                    self.out = True
                    return
            else:
                break

    def reached_powerup(self):
        x, y = self.targeting.rect.center
        if self.collide(x, y):
            self.targeting.power_up(self)
            self.curr_path = self.main_path
            self.find_main_pathpos()
            self.path_pos = self.main_path_pos
            return True
        return False
