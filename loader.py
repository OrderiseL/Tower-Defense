import pygame
import settings
import A_STAR_pathfinding as asp

"""For map grid"""
map_grid = asp.process_to_grid(r"used_assets\cleaned.png")
node_grid = asp.create_node_grid(map_grid)
"""For Towers:"""
# load long tower imgs
ltower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\archer_1\{}.png".format(c)), (settings.tower_width, settings.tower_height))
    for c in range(7, 10)]
# load long archer imgs
larcher_imgs = [pygame.image.load(
    r"used_assets\Towers\archer_top1\{}.png".format(c))
    for c in range(38, 43)]
for i in range(len(larcher_imgs)):
    img = larcher_imgs[i]
    larcher_imgs[i] = pygame.transform.scale(img, (settings.archer_width, settings.archer_height))

# load short tower imgs
stower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\archer_2\{}.png".format(c)), (settings.tower_width, settings.tower_height))
    for c in range(10, 13)]
# load short archer imgs
sarcher_imgs = [pygame.image.load(
    r"used_assets\Towers\archer_top2\{}.png".format(c))
    for c in range(51, 57)]
for i in range(len(sarcher_imgs)):
    img = sarcher_imgs[i]
    sarcher_imgs[i] = pygame.transform.scale(img, (settings.archer_width, settings.archer_height))

# load range tower imgs
rtower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\range\{}.png".format(c)), (settings.tower_width, settings.tower_height))
    for c in range(4, 7)]

# load speed tower imgs
sptower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\speed\{}.png".format(c)), (settings.tower_width, settings.tower_height))
    for c in range(7, 10)]

"""For Enemies:"""
# powerup:
powerup_img = pygame.transform.scale(pygame.image.load(r"used_assets\enemies\crystal_2.png"), (20, 20))
# Load wizard imgs.
wiz_images = []
enemy_width = 40
enemy_height = 40
for c in range(20):
    if c < 10:
        wiz_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\2\2_enemies_1_run_00" + str(c) + ".png"),
            (settings.wiz_width, settings.wiz_height))
        )
    else:
        wiz_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\2\2_enemies_1_run_0" + str(c) + ".png"),
            (settings.wiz_width, settings.wiz_height)))

# load scorpion imgs
sc_images = []
for c in range(20):
    if c < 10:
        sc_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\1\1_enemies_1_run_00" + str(c) + ".png"),
            (settings.sc_width, settings.sc_height))
        )
    else:
        sc_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\1\1_enemies_1_run_0" + str(c) + ".png"),
            (settings.sc_width, settings.sc_height))
        )

# load clubber imgs
cl_images = []
for c in range(20):
    if c < 10:
        cl_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\5\5_enemies_1_run_00" + str(c) + ".png"),
            (settings.cl_width, settings.cl_height))
        )
    else:
        cl_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\5\5_enemies_1_run_0" + str(c) + ".png"),
            (settings.cl_width, settings.cl_height))
        )

"""Menu:"""
menu_bg = pygame.transform.scale(pygame.image.load(r"used_assets/menu.png"), (100, 60))
upgrade_img = pygame.transform.scale(pygame.image.load(r"used_assets/menu/upgrade.png"), (50, 50))
pause_img = pygame.transform.scale(pygame.image.load(r"used_assets/menu/button_pause.png"), (110, 110))
start_img = pygame.transform.scale(pygame.image.load(r"used_assets/menu/button_start.png"), (110, 110))
star = pygame.transform.scale(pygame.image.load(r"used_assets/star.png"), (40, 40))
vert_menu_bg = pygame.transform.scale(pygame.image.load(r"used_assets/menu/window_3.png"), (120, 600))
wave_img = pygame.transform.scale(pygame.image.load(r"used_assets/wave.png"), (250, 100))
# Buy stuff:
buy_long = pygame.transform.scale(pygame.image.load(r"used_assets/buy_long.png"), (90, 90))
buy_range = pygame.transform.scale(pygame.image.load(r"used_assets/buy_range.png"), (90, 90))
buy_short = pygame.transform.scale(pygame.image.load(r"used_assets/buy_short.png"), (90, 90))
buy_speed = pygame.transform.scale(pygame.image.load(r"used_assets/buy_speed.png"), (90, 90))
# Main menu
play_img = pygame.transform.scale(pygame.image.load(r"used_assets/menu/button_play.png"), (90, 90))
music_img = pygame.transform.scale(pygame.image.load(r"used_assets/menu/button_sound.png"), (110, 110))
musicoff_img = pygame.transform.scale(pygame.image.load(r"used_assets/menu/button_sound_off.png"), (110, 110))


def convert_alpha():
    for i in range(len(wiz_images)):
        wiz_images[i] = wiz_images[i].convert_alpha()
    for i in range(len(sc_images)):
        sc_images[i] = sc_images[i].convert_alpha()
    for i in range(len(cl_images)):
        cl_images[i] = cl_images[i].convert_alpha()
    for i in range(len(sarcher_imgs)):
        sarcher_imgs[i] = sarcher_imgs[i].convert_alpha()
    for i in range(len(larcher_imgs)):
        larcher_imgs[i] = larcher_imgs[i].convert_alpha()