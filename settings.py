import pygame

"""A Module to store all Constants for modules"""

# Screen settings
win_width = 1500
win_height = 900
bg = pygame.image.load(r"used_assets\pretty_bg.png")
bg = pygame.transform.scale(bg, (win_width, win_height))

"""For Towers:"""
tower_height = 100
tower_width = 90
archer_height = 40
archer_width = 40

"""For enemies"""
# Wizard
wiz_width = 60
wiz_height = 60
# Scorpion
sc_width = 50
sc_height = 50
# Clubber
cl_width = 80
cl_height = 80
