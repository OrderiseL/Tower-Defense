import pygame
import settings
import load_assets

pygame.font.init()


class Button:
    """
    Button class for menu objects
    """

    def __init__(self, menu, img, name):
        self.name = name
        self.img = img
        self.x = menu.x + 2
        self.y = menu.y - 7
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def clicked(self, x, y):
        """
        Returns if tower has been clicked and selects tower.
        :param x:
        :param y:
        :return: bool
        """
        if (self.width + self.x) >= x >= self.x \
                and (self.height + self.y) >= y >= self.y:
            self.selected = True
            return True
        self.selected = False
        return False

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))


class Menu:
    """Menu for holding buttons"""

    def __init__(self, x, y, tower):
        # For visuals:
        self.font = pygame.font.SysFont("comicsans", 60)
        self.bg = load_assets.menu_bg
        # Attributes:
        self.x = x
        self.y = y
        self.width = self.bg.get_width()
        self.height = self.bg.get_height()
        # Items:
        self.buttons = []
        self.item_count = 0
        # For interactions:

    def draw(self, screen):
        screen.blit(self.bg, (self.x, self.y - 10))
        for item in self.buttons:
            item.draw(screen)

    def add_item(self, img, name):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.item_count += 1
        inc_x = self.width / self.item_count / 2
        self.buttons.append(Button(self, img, name))

    def is_clicked(self, x, y):
        """
        returns the selected item from the menu
        :param x: int
        :param y: int
        :return: string
        """
        for item in self.buttons:
            if item.clicked(x, y):
                return item.name
        return None
