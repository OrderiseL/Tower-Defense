import pygame
import math
import settings
from menu.menu import Menu
import loader


class Tower:
    def __init__(self, x, y):
        # For visuals:
        self.tower_imgs = []
        self.x = x
        self.y = y
        self.width, self.height = (settings.tower_width, settings.tower_height)
        # Attributes:
        self.cost = 0
        self.type = ""
        self.upgrade_cost = [2000, 5000, "MAX"]
        self.sell_cost = [2000, 5000, 12000]
        self.level = 1
        self.range = 150
        self.curr_range = self.range
        self.in_range = False
        # For interactions:
        self.selected = False
        self.moving = False
        # Define menu
        self.menu = Menu(self.x - 100, self.y, self)
        self.menu.add_item(loader.upgrade_img, "upgrade")

    def draw(self, screen):
        """
        draws the tower according to state(moving/placed)
        :param screen: Surface
        :return: None
        """
        if self.moving:
            self._draw_moving(screen)
            return
            # draw range circle:
        if self.selected:
            circle = pygame.Surface((self.curr_range * 4, self.curr_range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(circle, (128, 128, 128, 100), (self.curr_range, self.curr_range), self.curr_range, 0)
            screen.blit(circle, (self.x - self.curr_range, self.y - self.curr_range))
        # Draw tower:
        img = self.tower_imgs[self.level - 1]
        screen.blit(img, (self.x - self.width // 2, self.y - self.height // 2))
        # Draw menu:
        if self.selected:
            self.menu.draw(screen)

    def draw_placement(self, screen):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (200, 0, 0,100), (50, 50), 50, 0)

        screen.blit(surface, (self.x - 50, self.y - 50))

    def click(self, x, y):
        """
        Returns if tower has been clicked and selects tower.
        :param x:
        :param y:
        :return: bool
        """
        if (self.width // 2 + self.x) >= x >= (self.x - self.width // 2) \
                and (self.height // 2 + self.y) >= y >= (self.y - self.height // 2):
            self.selected = True
            return True
        self.selected = False
        return False

    def sell(self):
        """
        call to sell tower
        :return: int
        """
        pass

    def upgrade(self, money):
        """
        upgrade tower for defined cost and return if successful
        :return: price
        """
        if self.level < len(self.upgrade_cost):
            price = self.upgrade_cost[self.level - 1]
            if money >= price:
                self.level += 1
                return price
        return 0

    def move(self, x, y):
        """
        Allows to move tower
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y
        self.menu.update(x, y)

    def _check_inrange(self, x, y):
        """
        Checks if postion is in range of tower and updates
        :param x: int
        :param y: int
        :return: None
        """
        dis = math.dist((self.x, self.y), (x, y))
        if dis < self.curr_range:
            return True
        return False

    def _draw_moving(self, screen):
        # draw range circle:
        circle = pygame.Surface((self.curr_range * 2, self.curr_range * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(circle, (0, 128, 128, 100), (self.curr_range, self.curr_range), self.curr_range, 0)
        screen.blit(circle, (self.x - self.curr_range, self.y - self.curr_range))
        # Draw tower:
        img = self.tower_imgs[self.level - 1]
        screen.blit(img, (self.x - self.width // 2, self.y - self.height // 2))

    def has_collided(self, other):
        """
        returns true if tower is on another.
        :param other: Tower
        :return: bool
        """
        x2 = other.x
        y2 = other.y

        dist = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        if dist >= self.height:
            return False
        else:
            return True

