import pygame, PIL.Image
from enemies.enemy_types import *
import settings
from towers.tower_types import *
import random
import time
from menu.menu import VerticalMenu, PlayPauseButton
import loader
from enemies.powerboost import Powerup

pygame.init()
pygame.font.init()

heart = pygame.transform.scale(pygame.image.load("used_assets\heart.png"), (60, 60))  # For health
star_img = pygame.transform.scale(pygame.image.load(r"used_assets\star.png"), (60, 60))  # For money
font = pygame.font.SysFont("comicsans", 70)

waves = [
    [4, 0, 0],
    [5, 2, 0],
    [3, 2, 1],
    [1, 2, 2],
    [3, 4, 0],
    [0, 4, 1],
    [0, 4, 3],
    [0, 0, 7],
    [20, 100, 0],
    [50, 100, 0],
    [100, 100, 0],
    [0, 0, 50],
    [20, 0, 100],
    [20, 0, 150],
    [200, 100, 200],
]
# for music
pygame.mixer.music.load(r"used_assets\On_The_Horizon.mp3")
# pygame.mixer.music.set_volume(0)


class Game:

    def __init__(self):
        self.active = True
        self.timer = time.time()
        self.pb_timer = time.time()
        # initalize main window settings
        self.screen = pygame.display.set_mode((settings.win_width, settings.win_height))
        settings.bg = settings.bg.convert_alpha()
        loader.convert_alpha()
        # Enemies:
        self.powerups = pygame.sprite.Group()
        self.enemies = []
        # For towers:
        self.attack_towers = []
        self.support_towers = []
        self.selected_tower = None
        self.moving_object = None
        # Player resources
        self.lives = 10
        self.money = 600
        # Gameplay values:
        self.pause = True
        self.wave_num = 1
        self.current_wave = waves[self.wave_num - 1][:]
        # Buttons:
        self.buy_menu = VerticalMenu(settings.win_width, 170)
        self.play_pause_btn = PlayPauseButton(10, settings.win_height - 120)
        self.music_btn = PlayPauseButton(self.play_pause_btn.width + 30, settings.win_height - 120)
        self.music_btn.play_img = loader.music_img
        self.music_btn.img = loader.music_img
        self.music_btn.pause_img = loader.musicoff_img

    def run(self):
        """Function to run game"""
        self._update_screen()
        clock = pygame.time.Clock()
        pygame.mixer.music.play(1)
        while self.active:
            clock.tick(60)  # Limit framerate
            self._check_events()
            if not self.pause:
                # spawn powerboost:
                if (time.time() - self.pb_timer) >= random.randrange(5, 6) and len(self.powerups) <= 5:
                    self.pb_timer = time.time()
                    self.spawn_powerboost()
                # spawn new enemies:
                if time.time() - self.timer >= random.randrange(1, 6) / 3:
                    self.timer = time.time()
                    self._spawn_wave()
                self._handle_enemies()
                if self.lives == 0:
                    print("Lost")
                    self.active = False
                    break
            self._handle_towers()
            self._update_screen()
        pygame.quit()

    def _spawn_wave(self):
        """
        generate the next enemy or enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave_num += 1
                self.current_wave = waves[self.wave_num - 1]
                self.pause = True
                self.moving_object = None
                self.selected_tower = None
                self.play_pause_btn.change_img()
        else:
            wave_enemies = [Scorpion(), Wizard(), Clubber()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exit")
                self.active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_RIGHT:
                    self.moving_object = None
                else:
                    self._mouse_down_events()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pos = pygame.mouse.get_pos()
                    self.powerups.add(Powerup(pos))

    def _mouse_down_events(self):
        """
        Handles mouse press events
        :return: None
        """
        pos = pygame.mouse.get_pos()
        # click on music button:
        if self.music_btn.clicked(pos[0], pos[1]):
            self.music_btn.change_img()
            if self.music_btn.img == self.music_btn.pause_img:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            self.music_btn.draw(self.screen)
            pygame.display.update()
        # Click on play btn:
        if self.play_pause_btn.clicked(pos[0], pos[1]):
            self.pause = not self.pause
            self.play_pause_btn.change_img()
            self.play_pause_btn.draw(self.screen)
            pygame.display.update()
        # Handle tower placement:
        if self.moving_object:
            self._place_tower(pos)
        # Handle click on tower:
        elif not self._tower_press(pos):
            # Handle click on buy menu:
            self._menu_press(pos)

    def _tower_press(self, pos):
        """
        Handles if clicked on tower and returns if clicked
        :param pos: x,y
        :return: bool
        """
        clicked = False
        # Selected tower:
        btn_clicked = None
        if self.selected_tower:
            btn_clicked = self.selected_tower.menu.is_clicked(pos[0], pos[1])
            if btn_clicked:
                if btn_clicked == "upgrade":
                    price = self.selected_tower.upgrade(self.money)
                    self.money -= price
                    clicked = True
        if not btn_clicked:
            for tower in (self.support_towers + self.attack_towers):
                if tower.click(pos[0], pos[1]):
                    self.selected_tower = tower
                    clicked = True
        return clicked

    def _menu_press(self, pos):
        """
        Handles if clicked on menu and returns if clicked
        :param pos: x,y
        :return: bool
        """
        x, y = pos[:]
        name_list = ["range", "speed", "long", "short"]
        # Selected purchase:
        btn_clicked = self.buy_menu.is_clicked(x, y)
        if btn_clicked:
            cost = self.buy_menu.items_costs[btn_clicked]
            if cost <= self.money:
                obj_list = [RangeTower(x, y), SpeedTower(x, y), LongArcher(x, y), ShortArcher(x, y)]
                self.moving_object = obj_list[name_list.index(btn_clicked)]
                self.moving_object.cost = cost
                self.moving_object.moving = True

    def _place_tower(self, pos):
        if not self._is_valid_position(pos):
            return False
        # Place it.
        self.moving_object.moving = False
        if self.moving_object.type == "attack":
            self.attack_towers.append(self.moving_object)
        else:
            self.support_towers.append(self.moving_object)
        self.money -= self.moving_object.cost
        self.moving_object = None

    def _is_valid_position(self, pos):
        """
        Returns if not on menu,buttons,path..
        :param pos:
        :return: bool
        """
        r, c = asp.get_reverse_pos(pos)
        # check Tower not on path or other tower
        for tower in (self.support_towers + self.attack_towers):
            if self.moving_object.has_collided(tower):
                self.moving_object = None
                return False
        if loader.map_grid[r, c]:
            return False
        # Check tower not on menu:
        if self.buy_menu.is_clicked(pos[0], pos[1]):
            return False
        # Check buttons:
        if self.play_pause_btn.clicked(pos[0], pos[1]) or self.music_btn.clicked(pos[0], pos[1]):
            return False
        return True

    def _update_screen(self):
        # Draw background
        self.screen.blit(settings.bg, (0, 0))
        self._draw_objects()
        self._draw_possesions()
        # Draw buy menu
        self.buy_menu.draw(self.screen)

        pygame.display.update()

    def _draw_possesions(self):
        self.powerups.draw(self.screen)
        # Draw play btn
        self.play_pause_btn.draw(self.screen)
        self.music_btn.draw(self.screen)
        # Draw lives
        txt = font.render(str(self.lives), 1, (255, 255, 255))
        self.screen.blit(heart, (self.screen.get_width() - heart.get_width() - 10, 10))
        self.screen.blit(txt, (self.screen.get_width() - heart.get_width() - txt.get_width() - 10, 10))
        # Draw money
        txt = font.render(str(self.money), 1, (255, 255, 255))
        self.screen.blit(star_img, (self.screen.get_width() - star_img.get_width() - 10, 10 + heart.get_height()))
        self.screen.blit(txt, (
            self.screen.get_width() - star_img.get_width() - txt.get_width() - 10, 10 + heart.get_height()))
        # Draw wave
        txt = font.render("Wave #" + str(self.wave_num), 1, (255, 255, 255))
        self.screen.blit(wave_img, (10, 10))
        self.screen.blit(txt, (40, 40))

    def _draw_objects(self):

        # Draw objects
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for tower in (self.support_towers + self.attack_towers):
            if self.moving_object:
                tower.draw_placement(self.screen)
            tower.draw(self.screen, self.pause)

        if self.moving_object:
            self.moving_object.draw(self.screen, self.pause)

    def _handle_towers(self):
        # Check attack_towers:
        if not self.pause:
            if self.enemies:
                for tw in self.attack_towers:
                    self.money += tw.attack(self.enemies)
            # Support towers:
            for tower in self.support_towers:
                tower.support(self.attack_towers)
                tower.support(self.support_towers)
        if self.moving_object:
            pos = pygame.mouse.get_pos()
            self.moving_object.move(pos[0], pos[1])

    def _handle_enemies(self):
        # Check enemies:
        for e in self.enemies:
            # Enemies passed end.
            if e.out:
                self.lives -= 1
                self.enemies.remove(e)
                continue
            elif e.dead:  # killed
                self.enemies.remove(e)
                continue
            # Reached powerup:
            if isinstance(e.targeting, Powerup):
                if e.reached_powerup():
                    self.powerups.remove(e.targeting)
                    e.targeting = -1
            e.move()
        # Move to powerup
        for pb in self.powerups:
            if not pb.is_targeted:
                for e in self.enemies:
                    if e.targeting is None:
                        e.move_to_powerup(pb)
                        break

    def spawn_powerboost(self):
        r = c = 0
        rows, cols = map_grid.shape
        while not map_grid[r + 2, c] or not map_grid[r, c + 2] or not map_grid[r - 2, c]:
            r = random.randrange(10, rows - 10)
            c = random.randrange(10, cols - 2)
        x, y = asp.get_pos((r, c))
        self.powerups.add(Powerup((x, y)))


if __name__ == '__main__':
    g = Game()
    g.run()
