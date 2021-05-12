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

    def update_pos(self):
        self.x = self.menu.x + 2
        self.y = self.menu.y - 7


class Menu:
    """Menu for holding buttons"""

    def __init__(self, x, y, tower):
        # For visuals:
        self.font = pygame.font.SysFont("comicsans", 22)
        self.bg = load_assets.menu_bg
        # Attributes:
        self.tower = tower
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
            screen.blit(load_assets.star, (item.x + item.width + 2, item.y - 5))
            txt = self.font.render(str(self.tower.upgrade_cost[self.tower.level - 1]), 1, (240, 255, 255))
            screen.blit(txt, (item.x + item.width + 4, item.y + load_assets.star.get_height()))

    def add_item(self, img, name):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.item_count += 1
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

    def update(self, x, y):
        self.x = x
        self.y = y
        for btn in self.buttons:
            btn.update_pos()


class VerticalButton(Button):
    def __init__(self, menu, img, name):
        super().__init__(menu, img, name)
        self.y += self.menu.item_count * 10 + 1.5 * self.height * self.menu.item_count + 10


class VerticalMenu(Menu):
    """Menu for buying towers"""

    def __init__(self, x, y):
        super().__init__(x, y, None)
        self.bg = load_assets.vert_menu_bg
        self.width = self.bg.get_width()
        self.height = self.bg.get_height()
        self.items_costs = {"range": 800, "speed": 800, "long": 500, "short": 500}
        self.x -= self.width
        self._create_buttons()

    def draw(self, screen):
        screen.blit(self.bg, (self.x, self.y - 10))
        for item in self.buttons:
            item.draw(screen)
            st = pygame.transform.scale(load_assets.star, (30, 30))
            screen.blit(st, (item.x + 5, item.y + item.height + 2))
            txt = self.font.render(str(self.items_costs[item.name]), 1, (240, 255, 255))
            screen.blit(txt, (item.x + 5 + st.get_width(), item.y + item.height + 10))

    def _create_buttons(self):
        self.buttons.append(VerticalButton(self, load_assets.buy_long, "long"))
        self.item_count += 1
        self.buttons.append(VerticalButton(self, load_assets.buy_short, "short"))
        self.item_count += 1
        self.buttons.append(VerticalButton(self, load_assets.buy_range, "range"))
        self.item_count += 1
        self.buttons.append(VerticalButton(self, load_assets.buy_speed, "speed"))
        self.item_count += 1
