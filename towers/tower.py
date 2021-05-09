import pygame


class Tower:
    def __init__(self, x, y):
        # For visuals:
        self.tower_imgs = []
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        # Attributes:
        self.upgrade_cost = [0, 0, 0]
        self.sell_cost = [0, 0, 0]
        self.level = 1
        self.range = 100
        # For interactions:
        self.selected = False
        self.menu = None

    def draw(self, screen):
        """
        draws the tower
        :param screen:
        :return:
        """
        # draw range circle:
        circle = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(circle, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
        screen.blit(circle, (self.x - self.range, self.y - self.range))
        # Draw tower:
        img = self.tower_imgs[self.level - 1]
        screen.blit(img, (self.x - self.width // 2, self.y - self.height // 2))

    def click(self, x, y):
        """
        Returns if tower has been clicked and selects tower.
        :param x:
        :param y:
        :return: bool
        """
        if (self.width + self.x) >= x >= self.x \
                and (self.height + self.y) >= y >= self.y:
            return True
        pass

    def sell(self):
        """
        call to sell tower
        :return: int
        """
        pass

    def upgrade(self):
        """
        upgrade tower for defined cost
        :return:
        """
        self.level += 1

    def move(self, x, y):
        """
        Allows to move tower
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y
