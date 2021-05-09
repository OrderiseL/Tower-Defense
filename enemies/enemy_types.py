import pygame
from enemies.enemy import Enemy

# Load wizard imgs.
wiz_images = []
w_width = 30
w_height = 30
for c in range(20):
    if c < 10:
        wiz_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\2\2_enemies_1_run_00" + str(c) + ".png"),
            (w_width, w_height))
        )
    else:
        wiz_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\2\2_enemies_1_run_0" + str(c) + ".png"),
            (w_width, w_height)))
# load scorp imgs
sc_images = []
for c in range(20):
    if c < 10:
        sc_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\1\1_enemies_1_run_00" + str(c) + ".png"),
            (w_width, w_height))
        )
    else:
        sc_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\1\1_enemies_1_run_0" + str(c) + ".png"),
            (w_width, w_height))
        )
# load clubber imgs
cl_images = []
for c in range(20):
    if c < 10:
        cl_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\5\5_enemies_1_run_00" + str(c) + ".png"),
            (40, 40))
        )
    else:
        cl_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\5\5_enemies_1_run_0" + str(c) + ".png"),
            (40, 40))
        )


class Wizard(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.max_health = 3
        self.health = self.max_health
        # Load for animation:
        self.images = wiz_images[:]


class Scorpion(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.max_health = 1
        self.health = self.max_health
        # Load for animation:
        self.images = sc_images[:]


class Clubber(Enemy):

    def __init__(self):
        super().__init__()
        # Attributes:
        self.max_health = 5
        self.health = self.max_health
        # Load for animation:
        self.width = 40
        self.height = 40
        self.images = cl_images[:]
