import pygame
from towers.tower import Tower
import math

# load tower imgs
ltower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\archer_1\{}.png".format(c)), (60, 60))
    for c in range(7, 10)]
# load archer imgs
larcher_imgs = [pygame.image.load(
    r"used_assets\Towers\archer_top1\{}.png".format(c))
    for c in range(38, 43)]
for i in range(len(larcher_imgs)):
    img = larcher_imgs[i]
    larcher_imgs[i] = pygame.transform.scale(img, (int(img.get_width() * 0.5), int(img.get_height() * 0.5)))

class LongArcher(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        # For animation:
        self.archer_frame = 0
        self.left = False
        # load tower imgs
        self.tower_imgs = ltower_imgs[:]
        # load archer imgs
        self.archer_imgs = larcher_imgs[:]

        # For attacking.
        self.damage = 1
        self.attack_speed = 0.15
        self.range = self.range * 1.5
        self.in_range = False
        self.end = False

    def draw(self, screen):
        super().draw(screen)
        # Draw attacking motion
        if self.in_range:
            self.end = False
            self.archer_frame += self.attack_speed
        else:
            self.archer_frame = 0
        if int(self.archer_frame) >= len(self.archer_imgs):
            self.end = True
            self.archer_frame = 0
        archer = self.archer_imgs[int(self.archer_frame)]
        archer = pygame.transform.flip(archer, self.left, False)
        # draw archer at middle of tower.
        screen.blit(archer, (self.x - 12, self.y - archer.get_height() - 17))

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, updates list
        :param enemies: enemies list
        :return: None
        """

        closest_enemy = []
        for enemy in enemies:
            en_x = enemy.x + enemy.width
            en_y = enemy.y + enemy.height
            if self._check_inrange(en_x, en_y):
                self.in_range = True
                closest_enemy.append(enemy)
        if closest_enemy:
            closest_enemy.sort(key=lambda en: en.x)
            first = closest_enemy[0]
            self._update_direction(first.x, first.y)
            # Attack when archer finished motion.
            if self.end:
                if first.hit(self.damage):
                    closest_enemy.remove(first)
        else:
            self.in_range = False

    def _check_inrange(self, x, y):
        """
        Checks if postion is in range of tower and updates
        :param x: int
        :param y: int
        :return: None
        """
        dis = math.dist((self.x, self.y), (x, y))
        if dis < self.range:
            return True
        return False

    def _update_direction(self, x, y):
        """
        Check if coors are to left or right of tower and update
        :param x: int
        :param y: int
        :return: None
        """
        if self.x > x:
            self.left = True
        else:
            self.left = False

    def upgrade(self):
        super().upgrade()
        self.damage += 1


# load tower imgs
stower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\archer_2\{}.png".format(c)), (60, 60))
    for c in range(10, 13)]
# load archer imgs
sarcher_imgs = [pygame.image.load(
    r"used_assets\Towers\archer_top2\{}.png".format(c))
    for c in range(44, 51)]
for i in range(len(sarcher_imgs)):
    img = sarcher_imgs[i]
    sarcher_imgs[i] = pygame.transform.scale(img, (int(img.get_width() * 0.5), int(img.get_height() * 0.5)))


class ShortArcher(LongArcher):
    def __init__(self, x, y):
        super().__init__(x, y)
        # For animation.
        self.archer_imgs = sarcher_imgs[:]
        self.tower_imgs = stower_imgs[:]
        # For attacks:
        self.damage = 2
        self.attack_speed = 0.15
        self.range = self.range * 0.6


if __name__ == '__main__':
    la = LongArcher(0, 0)
