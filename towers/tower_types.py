from towers.tower import Tower
from loader import *
from projectile import Arrow


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
        self.type = "attack"
        # For attacking.
        self.arrows = pygame.sprite.Group()
        self.damage = 1
        self.attack_speed = 0.15
        self.curr_speed = self.attack_speed
        self.range = self.range * 1.5
        self.curr_range = self.range
        self.end = False

    def draw(self, screen, paused):
        """
        Draw tower+radius then animated archers
        :param screen: Surface
        :return: None
        """
        super().draw(screen, paused)
        archer = self.archer_imgs[int(self.archer_frame)]
        if not self.moving and not paused:
            # Draw attacking motion
            if self.in_range:
                self.end = False
                self.archer_frame += self.curr_speed
            else:
                self.archer_frame = 0
            if int(self.archer_frame) >= len(self.archer_imgs):
                self.end = True
                self.archer_frame = 0
            archer = self.archer_imgs[int(self.archer_frame)]
            archer = pygame.transform.flip(archer, self.left, False)
            self.arrows.update()
        # draw archer at middle of tower.
        screen.blit(archer, (self.x - 25, self.y - 70))
        # Draw arrows
        self.arrows.draw(screen)

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, updates list
        :param enemies: enemies list
        :return: None
        """
        worth = 0
        closest_enemy = []
        for enemy in enemies:
            en_x = enemy.x
            en_y = enemy.y
            dis = self._check_inrange(en_x, en_y)
            dis2 = self._check_inrange(en_x, en_y + enemy.height)
            if dis:
                self.in_range = True
                closest_enemy.append((dis, enemy))
            elif dis2:
                self.in_range = True
                closest_enemy.append((dis2, enemy))
        if closest_enemy:
            closest_enemy.sort(key=lambda dat: dat[0])
            first = closest_enemy[0][1]
            self._update_direction(first.x, first.y)
            # Attack when archer finished motion.
            if self.end:
                arrow = Arrow(first, (self.x, self.y - 70))
                self.arrows.add(arrow)
        else:
            self.in_range = False

        for arrow in self.arrows:
            res = arrow.hit_target(self.damage)
            if res != -2:
                self.arrows.remove(arrow)
                worth+=res
        return worth

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

    def upgrade(self, money):
        price = super().upgrade(money)
        if price:
            self.damage += 1
        return price


class ShortArcher(LongArcher):
    def __init__(self, x, y):
        super().__init__(x, y)
        # For animation.
        self.archer_imgs = sarcher_imgs[:]
        self.tower_imgs = stower_imgs[:]
        # For attacks:
        self.damage = 2
        self.attack_speed = 0.15
        self.curr_speed = self.attack_speed
        self.range = self.range * 0.6
        self.curr_range = self.range


# Support towers:
class RangeTower(Tower):
    """
       Increases attack range
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "support"

        self.effect = [0.2, 0.4, 0.6]
        self.tower_imgs = rtower_imgs

    def support(self, towers):
        """
        modify towers according to ability
        :param towers: list
        :return:
        """
        affected = []
        for tower in towers:
            to_x = tower.x + tower.width
            to_y = tower.y + tower.height
            if self._check_inrange(to_x, to_y):
                self.in_range = True
                affected.append(tower)
        for tower in affected:
            tower.curr_range = tower.range + round(tower.range * self.effect[self.level - 1])


class SpeedTower(Tower):
    """
    Increases attack speed
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "support"
        self.effect = [0.2, 0.3, 0.4]
        self.tower_imgs = sptower_imgs

    def support(self, towers):
        """
        modify towers according to ability
        :param towers: list
        :return:
        """
        affected = []
        for tower in towers:
            to_x = tower.x + tower.width
            to_y = tower.y + tower.height
            if self._check_inrange(to_x, to_y):
                self.in_range = True
                affected.append(tower)
        for tower in affected:
            if tower.type == "support":
                return
            tower.curr_speed = tower.attack_speed + tower.attack_speed * self.effect[self.level - 1]


if __name__ == '__main__':
    la = LongArcher(0, 0)
