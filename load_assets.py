import pygame
import settings

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
    larcher_imgs[i] = pygame.transform.scale(img, (int(img.get_width() * 0.7), int(img.get_height() * 0.7)))

# load short tower imgs
stower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\archer_2\{}.png".format(c)), (settings.tower_width, settings.tower_height))
    for c in range(10, 13)]
# load short archer imgs
sarcher_imgs = [pygame.image.load(
    r"used_assets\Towers\archer_top2\{}.png".format(c))
    for c in range(44, 51)]
for i in range(len(sarcher_imgs)):
    img = sarcher_imgs[i]
    sarcher_imgs[i] = pygame.transform.scale(img, (int(img.get_width() * 0.7), int(img.get_height() * 0.7)))

# load range tower imgs
rtower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\range\{}.png".format(c)), (settings.tower_width, settings.tower_height))
    for c in range(4, 7)]

# load speed tower imgs
sptower_imgs = [pygame.transform.scale(pygame.image.load(
    r"used_assets\Towers\speed\{}.png".format(c)), (settings.tower_width, settings.tower_height))
    for c in range(7, 10)]

"""For Enemies:"""
# Load wizard imgs.
wiz_images = []
w_width = 30
w_height = 30
for c in range(20):
    if c < 10:
        wiz_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\2\2_enemies_1_run_00" + str(c) + ".png"),
            (w_width, w_height))
        )
    else:
        wiz_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\2\2_enemies_1_run_0" + str(c) + ".png"),
            (w_width, w_height)))

# load scorp imgs
sc_images = []
for c in range(20):
    if c < 10:
        sc_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\1\1_enemies_1_run_00" + str(c) + ".png"),
            (w_width, w_height))
        )
    else:
        sc_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\1\1_enemies_1_run_0" + str(c) + ".png"),
            (w_width, w_height))
        )

# load clubber imgs
cl_images = []
for c in range(20):
    if c < 10:
        cl_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\5\5_enemies_1_run_00" + str(c) + ".png"),
            (40, 40))
        )
    else:
        cl_images.append(pygame.transform.scale(
            pygame.image.load(r"used_assets\enemies\5\5_enemies_1_run_0" + str(c) + ".png"),
            (40, 40))
        )

"""Menu:"""
menu_bg = pygame.transform.scale(pygame.image.load(r"used_assets\menu.png"), (100, 60))
upgrade_img = pygame.transform.scale(pygame.image.load(r"used_assets\menu\upgrade.png"), (40, 40))
pause_img = pygame.transform.scale(pygame.image.load(r"used_assets\menu\button_pause.png"), (30, 20))
play_img = pygame.transform.scale(pygame.image.load(r"used_assets\menu\button_play.png"), (30, 20))
star = pygame.transform.scale(pygame.image.load(r"used_assets\star.png"), (40, 40))
star_2 = pygame.transform.scale(pygame.image.load(r"used_assets\star.png"), (20, 20))

