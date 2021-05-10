import pygame

"""A Module to store all Constants for modules"""

# Screen settings
scr_width = 1000
scr_height = 600
bg = pygame.image.load(r"used_assets\game_background_2.png")
bg = pygame.transform.scale(bg, (scr_width, scr_height))

"""For Towers:"""
tower_height = 70
tower_width = 70
