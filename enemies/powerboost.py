import pygame
from loader import powerup_img

"""
A power-up that will spawn every couple of seconds.
Enemies that havent passed the power-up will move towards it.
Challenges:
1. Movement- without getting out of path.
if 
"""


class Powerup(pygame.sprite.Sprite):

    def __init__(self, pos):
        """
        :param pos: position.
        """
        super(Powerup, self).__init__()
        self.image = powerup_img
        self.rect = self.image.get_rect()
        self.rect.center = pos
        # Special
        self.is_targeted = False
        self.boost = 2  # multiply health, increase size.

    def power_up(self, enemy):
        """
        Increases attributes
        :return: none
        """
        enemy.health *= self.boost
        enemy.max_health = enemy.health
        enemy.width = int(enemy.width * 1.5)
        enemy.height = int(enemy.height * 1.5)
        for i in range(len(enemy.images)):
            new_img = pygame.transform.scale(enemy.images[i], (enemy.width, enemy.height))
            enemy.images[i] = new_img
