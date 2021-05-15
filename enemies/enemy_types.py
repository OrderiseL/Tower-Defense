from enemies.enemy import Enemy
from loader import *


class Wizard(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.worth = 50
        self.max_health = 3
        self.health = self.max_health
        # Load for animation:
        self.images = wiz_images[:]


class Scorpion(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.worth = 30
        self.max_health = 1
        self.health = self.max_health
        # Load for animation:
        self.images = sc_images[:]


class Clubber(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.worth = 80
        self.max_health = 5
        self.health = self.max_health
        # Load for animation:
        self.width = 40
        self.height = 40
        self.images = cl_images[:]
