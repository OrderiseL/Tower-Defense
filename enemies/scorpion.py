import pygame
from enemies.enemy import Enemy


class Scorpion(Enemy):
    images = []
    for c in range(20):
        if c < 10:
            images.append(
                pygame.image.load(r"used_assets\enemies\scorp\1_enemies_1_run_00" + str(c) + ".png"))
        else:
            images.append(
                pygame.image.load(r"used_assets\enemies\scorp\1_enemies_1_run_0" + str(c) + ".png"))

    def __init__(self):
        super().__init__()
