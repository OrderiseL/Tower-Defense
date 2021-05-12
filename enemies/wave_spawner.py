import pygame
import time

class WaveSpawner:
    """Class to spawn enemy waves"""

    def __init__(self,timer):
        # Attributes:
        self.time_btwn_waves = 5
        self.countdown = 2
        self.timer = timer

    def update(self):
        if self.countdown<=0:
            self.spawn_wave()

    def spawn_wave(self):
        pass