import pygame
import math


# TODO: Fix arrow homing

class Arrow(pygame.sprite.Sprite):

    def __init__(self, target, pos=(500, 500)):
        """
        :param target: Enemy
        :param pos: Where to spawn arrow
        """
        super(Arrow, self).__init__()
        # For animation:
        self.original_image = pygame.transform.scale(pygame.image.load(r"used_assets\Towers\arrow.png"), (20, 5))
        self.image = self.original_image
        self.angle = 0
        # For positioning:
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.target = target  # Enemy type.
        # Movement:
        self.add_y = 0
        self.add_x = 0
        self._update_move_values()

    def _calc_angle(self):
        """
        calculate angle using tan(m)
        :return: None
        """
        tx = self.target.x + self.target.width // 2
        ty = self.target.y + self.target.height // 2
        radians = math.atan2((ty - self.rect.y), (tx - self.rect.x))
        self.angle = math.degrees(radians)

    def hit_target(self, damage):
        """

        :return:
        """
        if self.target.dead:
            return -1
        if self.target.collide(self.rect.center[0], self.rect.center[1]):
            return self.target.hit(damage)
        return 0

    def update(self):
        self._update_move_values()
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        x, y = self.rect.center  # Save its current center.
        x += self.add_x
        y += self.add_y
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.

    def _update_move_values(self):
        """Calculates how to move according to point ratio"""
        self._calc_angle()
        tx = self.target.x + self.target.width // 2
        ty = self.target.y + self.target.height // 2
        start_p = list(self.rect.center)
        end_p = list((tx, ty))
        d = math.dist(start_p, end_p)
        xp = (start_p[0] * (d - self.speed) + end_p[0] * self.speed) / d
        yp = (start_p[1] * (d - self.speed) + end_p[1] * self.speed) / d
        self.add_x = xp - start_p[0]
        self.add_y = yp - start_p[1]
