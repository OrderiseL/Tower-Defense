import pygame


class Arrow(pygame.sprite.Sprite):

    def __init__(self, target, pos=(500, 500)):
        super(Arrow, self).__init__()
        # For animation:
        self.original_image = pygame.image.load(r"used_assets\Towers\arrow.png")
        self.curr_image = self.original_image
        self.angle = 0
        # For positioning:
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.target = target # Enemy type.

    def _calc_angle(self):
        pass

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 1 % 360  # Value will reapeat after 359. This prevents angle to overflow.
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.
