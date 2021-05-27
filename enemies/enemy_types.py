from enemies.enemy import Enemy
from loader import *


class Wizard(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.worth = 90
        self.max_health = 3
        self.health = self.max_health
        # Load for animation:
        self.images = wiz_images[:]


class Scorpion(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.width = settings.sc_width
        self.height = settings.sc_height
        self.worth = 33
        self.max_health = 1
        self.health = self.max_health
        # Load for animation:
        self.images = sc_images[:]


class Clubber(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.width = settings.cl_width
        self.height = settings.cl_height
        self.worth = 120
        self.max_health = 5
        self.health = self.max_health
        # Load for animation:
        self.images = cl_images[:]
