import pygame
import math
import settings


# TODO: Have some powerup spawn on map

class Enemy:
    """
    Abstract class for all enemies.
    """

    def __init__(self):
        # set attributes
        self.worth = 50
        self.width = settings.wiz_width
        self.height = settings.wiz_height
        self.speed = 3
        self.max_health = 3
        self.health = self.max_health
        self.path = [(-self.width, 293), (208, 294), (265, 324), (295, 355), (349, 370), (687, 364), (725, 342), (768, 281),
                     (784, 216), (813, 122), (859, 89), (945, 77), (1002, 103), (1028, 137), (1045, 189), (1051, 237),
                     (1059, 281), (1081, 315), (1133, 343), (1171, 350), (1255, 370), (1290, 407), (1313, 461),
                     (1306, 517), (1285, 570), (1254, 610), (1193, 631), (1142, 641), (1097, 647), (1051, 647),
                     (922, 654), (892, 662), (881, 677), (853, 700), (811, 716), (767, 719), (217, 715), (179, 699),
                     (138, 663), (119, 624), (111, 573), (99, 532), (80, 487),
                     (54, 461), (25, 435), (-self.width, 427)]

        # Movement and animation
        self.new_slope = False
        self.flipped = False
        self.animation_index = 0
        self.path_pos = 0
        self.images = []  # Class Variable
        self.img = None
        self.out = False
        self.dead = False
        # to adjust y
        for i in range(len(self.path)):
            self.path[i] = list(self.path[i])
            self.path[i][1] -= self.height // 2
        # Set position
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.add_y = 0  # Amount to add and keep even speed
        self.add_x = 0
        self._update_move_values()

    def draw(self, screen):
        """
        Draws the enemy
        :param screen: surface
        :return: None
        """
        if self.out:
            return
        # Set enemy
        self.move()
        # Draw enemy
        self.img = self.images[int(self.animation_index)]
        self.img = pygame.transform.flip(self.img, self.flipped, False)
        screen.blit(self.img, (int(self.x), int(self.y)))
        # Draw Health bar
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        """
        Draws health bar above enemy
        :param screen: Surface
        :return: None
        """
        length = self.width - 5
        h_increment = length / self.max_health
        curr_health = int(self.health * h_increment)
        pygame.draw.rect(screen, (80, 80, 80), (self.x, self.y - 10, length, 5), 0)
        pygame.draw.rect(screen, (0, 200, 0), (self.x, self.y - 10, curr_health, 5), 0)

    def move(self):
        """
        Moves enemy from current checkpoint to next one
        :return: None
        """
        # Increase to next frame
        self.animation_index += self.speed / 5
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.x += self.add_x
        self.y += self.add_y
        # Check postion when moving right or left.
        if self.add_x > 0:
            self.flipped = False
            # exceeded end position
            if (self.x + self.add_x) > self.path[self.path_pos + 1][0]:
                self.x = self.path[self.path_pos + 1][0]  # set at end position
                self.new_slope = True
        else:
            self.flipped = True  # moving left
            # exceeded end position
            if (self.x + self.add_x) < self.path[self.path_pos + 1][0]:
                self.x = self.path[self.path_pos + 1][0]  # set at end position
                self.new_slope = True
        # Check position moving Up or Down.
        if self.add_y > 0:  # Down
            # exceeded end position
            if (self.y + self.add_y) > self.path[self.path_pos + 1][1]:
                self.y = self.path[self.path_pos + 1][1]  # set at end position
                self.new_slope = True
        else:
            if (self.y + self.add_y) < self.path[self.path_pos + 1][1]:
                self.y = self.path[self.path_pos + 1][1]  # set at end position
                self.new_slope = True
        if self.new_slope:  # Calculate next x,y values
            self.path_pos += 1
            # Out of frame
            if (self.path_pos + 1) >= len(self.path):
                self.out = True
                return
            self._update_move_values()
            self.new_slope = False

    def _update_move_values(self):
        """Calculates how to move according to angle"""
        start_p = list((self.x, self.y))
        end_p = list(self.path[self.path_pos + 1])
        d = math.dist(start_p, end_p)
        xp = (start_p[0] * (d - self.speed) + end_p[0] * self.speed) / d
        yp = (start_p[1] * (d - self.speed) + end_p[1] * self.speed) / d
        self.add_x = xp - start_p[0]
        self.add_y = yp - start_p[1]

    def collide(self, x, y):
        """
        Return if position hit enemy
        :param x: int
        :param y: int
        :return:
        """
        if (self.width + self.x) >= x >= self.x \
                and (self.height + self.y) >= y >= self.y:
            return True
        return False

    def hit(self, damage):
        """
        Removes health and return if enemy has died
        :return: Bool
        """
        self.health -= damage
        if self.health <= 0:
            self.dead = True
            return self.worth
        return 0
