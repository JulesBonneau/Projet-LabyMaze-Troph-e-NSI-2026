import pyxel
import random
import time

SCREEN_WIDTH  = 160
SCREEN_HEIGHT = 120
LAVA_SPEEDS = [0.14, 0.2, 0.3 ]
COINS_PER_PX = 0.05

PACK_COST = 50

PLAYER_COLORS =[11, 9, 10, 14, 15, 6, 12, 13]

LEVEL_1_RECTS=[
    (0, 0, 2, 120), (158, 0, 2, 120), (0, 0, 132, 2), (0, 118, 160, 2),
    (85, 98, 2, 20), (60, 96, 27, 2), (0, 96, 27, 2), (27, 58, 2, 40), 
    (27, 58, 27, 2), (54, 58, 2, 20), (54, 78, 56, 2), (110, 78, 2, 22),
    (137, 58, 2, 62), (81, 58, 56, 2), (27, 38, 83, 2), (110, 38, 2, 22),
    (0, 18, 54, 2), (81, 18, 51, 2),
    (132, 0, 2, 42),]
LEVEL_2_RECTS=[
    (0, 0, 2, 120),(158, 0, 2, 120),(0, 0, 149, 2),(0, 118, 160, 2),
    (0, 105, 13, 2),(13, 77, 2, 30),(0, 68, 90, 2),(23, 68, 2, 39),
    (35, 95, 2, 12),(35, 95, 65, 2),(90, 68, 2, 17),(35, 85, 57, 2),
    (35, 77, 2, 8),(35, 77, 45, 2),(100, 50, 2, 56),(47, 105, 100, 2),
    (13, 58, 79, 2),(13, 40, 2, 18),(13, 40, 30, 2),(43, 50, 57, 2),
    (43, 40, 2, 10),(28, 51, 2, 7),(22, 51, 6, 2),(13, 13, 2, 15),
    (13, 13, 20, 2),(13, 28, 89, 2),(43, 0, 2, 30),(58, 13, 42, 2),
    (100, 13, 2, 17),(120, 0, 2, 42),(56, 40, 66, 2),(149, 0, 2, 42),
    (135, 17, 14, 2),(135, 17, 2, 15),(135, 42, 16, 2),(135, 42, 2, 25),
    (121, 67, 16, 2),(121, 50, 2, 18),(147, 52, 2, 55),(147, 52, 11, 2),
    (110, 78, 18, 2),(128, 78, 2, 12),(128, 90, 20, 2),(133, 90, 2, 7),
    (133, 97, 8, 2),]
LEVEL_3_RECTS = [
    (0, 0, 2, 120),(158, 0, 2, 120),(0, 0, 150, 2),(0, 118, 160, 2),
    (11, 84, 2, 34),(22, 67, 2, 51),(11, 67, 22, 2),(33, 67, 2, 34),
    (22, 19, 2, 34),(11, 51, 23, 2),(2, 34, 11, 2),(11, 17, 22, 2),
    (33, 17, 2, 17),(33, 34, 44, 2),(44, 2, 2, 34),(33, 85, 35, 2),
    (44, 101, 2, 17),(55, 86, 2, 17),(55, 34, 2, 17),(44, 51, 13, 2),
    (44, 51, 2, 17),(44, 68, 24, 2),(55, 17, 79, 2),(77, 34, 2, 35),
    (66, 51, 11, 2),(77, 68, 13, 2),(88, 68, 2, 17),(77, 85, 13, 2),
    (66, 101, 2, 17),(66, 101, 24, 2),(99, 68, 12, 2),(99, 68, 2, 34),
    (99, 101, 23, 2),(110, 101, 2, 17),(88, 17, 2, 35),(88, 51, 23, 2),
    (109, 34, 2, 17),(109, 68, 2, 17),(99, 34, 23, 2),(109, 2, 2, 17),
    (132, 17, 2, 51),(121, 68, 13, 2),(121, 51, 2, 17),(132, 34, 16, 2),
    (121, 85, 13, 2),(132, 85, 2, 18),(132, 101, 34, 2),(148, 2, 2, 17),
    (148, 51, 14, 2),(148, 51, 2, 19),(148, 85, 17, 2),(148, 101, 2, 17),]
ALL_LEVELS=[LEVEL_1_RECTS, LEVEL_2_RECTS, LEVEL_3_RECTS]

class Inventory: 
    def __init__(self):
        self.coins        = 0
        self.speed_boost  = 0
        self.lava_slow    = 0
        self.player_color = 11

class MapManager:
    BASE_SPEED=1
    def __init__(self, inventory: Inventory):
        self.inv   = inventory
        self.player_w  = 4
        self.player_h= 4
        self.current_level= 0
        self._coin_accum= 0.0
        self.load_level(0)

    @property
    def player_speed(self):
        return self.BASE_SPEED* (1 + 0.15 * self.inv.speed_boost)
    @property
    def lava_speed(self):
        return self._base_lava *(0.80 ** self.inv.lava_slow)

    def load_level(self, level_index):
        self.player_x=14
        self.player_y =111
        self._prev_y=111
        self.lava_y =SCREEN_HEIGHT
        self._base_lava=LAVA_SPEEDS[level_index]
        self.rectangles=list(ALL_LEVELS[level_index])
        self._spawn_pickups()

    def _spawn_pickups(self):
        self.pickups        = []  
        self.rainbow_active = False
        self.rainbow_timer  = 0
        attempts = 0
        while len(self.pickups) < 5 and attempts < 500:
            attempts += 1
            px=random.randint(4,SCREEN_WIDTH -8)
            py =random.randint(4, SCREEN_HEIGHT-20)
            if not self.check_collision(px, py) and not self.check_collision(px + 3, py + 3):
                self.pickups.append([px, py, True, 'normal'])

        if random.random() < 0.25:
            special_type = random.choice(['blue', 'red'])
            attempts = 0
            placed   = False
            while not placed and attempts < 500:
                attempts += 1
                zone = random.choice(['left', 'right', 'top'])
                if zone == 'left':
                    px = random.randint(3, 22)
                    py = random.randint(4, SCREEN_HEIGHT - 20)
                elif zone == 'right':
                    px = random.randint(138, SCREEN_WIDTH - 8)
                    py = random.randint(4, SCREEN_HEIGHT - 20)
                else:  # top
                    px = random.randint(4, SCREEN_WIDTH - 8)
                    py = random.randint(3, 18)
                if not self.check_collision(px, py) and not self.check_collision(px + 3, py + 3):
                    self.pickups.append([px, py, True, special_type])
                    placed = True

    def update(self):
        if self.lava_y > 1:
            self.lava_y -=self.lava_speed
        if self.player_y + self.player_h > self.lava_y:
            self.rainbow_active   = False
            self.inv.player_color = 11
            return "dead"

        delta_y = self._prev_y - self.player_y
        if delta_y > 0:
            self._coin_accum += delta_y * COINS_PER_PX
            whole = int(self._coin_accum)
            if whole > 0:
                self.inv.coins   += whole
                self._coin_accum -= whole
        self._prev_y = self.player_y



        if self.current_level == 0:
            if self.player_y < -2 and self.player_x < 149:
                self.current_level = 1
                self.load_level(1)
                return "next"
            if self.player_y < -2 and self.player_x >= 149:
                return "dead"
        elif self.current_level== 1:
            if self.player_y < -2:
                self.current_level = 2
                self.load_level(2)
                return "next"
        elif self.current_level==2:
            if self.player_y < -2:
                return "win"

        for pickup in self.pickups:
            if not pickup[2]:
                continue
            cx, cy = pickup[0], pickup[1]
            if (self.player_x < cx + 3 and self.player_x + self.player_w > cx and
                    self.player_y < cy + 3 and self.player_y + self.player_h > cy):
                pickup[2] = False
                if pickup[3] == 'normal':
                    self.inv.coins += 5
                elif pickup[3] == 'blue':
                    self.inv.coins += 20
                elif pickup[3] == 'red':
                    self.rainbow_active = True
                    self.rainbow_timer  = 0

        if self.rainbow_active:
            self.rainbow_timer += 1
            self.inv.player_color = PLAYER_COLORS[self.rainbow_timer // 6 % len(PLAYER_COLORS)]
        spd = self.player_speed
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            if not self.check_collision(self.player_x - spd, self.player_y):
                self.player_x -= spd
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            if not self.check_collision(self.player_x + spd, self.player_y):
                self.player_x += spd
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            if not self.check_collision(self.player_x, self.player_y - spd):
                self.player_y -= spd
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            if not self.check_collision(self.player_x, self.player_y + spd):
                self.player_y += spd

        self.player_x = max(2, min(self.player_x, SCREEN_WIDTH - self.player_w - 2))
        return None
        
        
        
    def check_collision(self, x, y):
        for rx, ry, rw, rh in self.rectangles:
            if (x + self.player_w > rx and x < rx + rw and
                    y + self.player_h > ry and y < ry + rh):
                return True
        return False



    def draw(self):
        pyxel.cls(0)
        for rx, ry, rw, rh in self.rectangles:
            pyxel.rect(rx, ry, rw, rh, 5)
        pyxel.rect(0, self.lava_y, 160, SCREEN_HEIGHT - self.lava_y, 8)
        pyxel.rect(self.player_x, self.player_y,
                   self.player_w, self.player_h, self.inv.player_color)

        for pickup in self.pickups:
            if not pickup[2]:
                continue
            color = 10 if pickup[3] == 'normal' else (12 if pickup[3] == 'blue' else 8)
            pyxel.rect(pickup[0], pickup[1], 3, 3, color)

        pyxel.text(2,  4, f"Niv {self.current_level + 1}/3", 7)
        pyxel.text(2, 12, f"$ {self.inv.coins}", 10)
        hud_x = 2
        if self.inv.speed_boost > 0:
            pyxel.text(hud_x, SCREEN_HEIGHT - 10, f"SPD x{self.inv.speed_boost}", 9)
            hud_x += 34
        if self.inv.lava_slow > 0:
            pyxel.text(hud_x, SCREEN_HEIGHT - 10, f"SLOW x{self.inv.lava_slow}", 14)





class PackScreen:
    def __init__(self, inventory: Inventory):
        self.inv= inventory
        self.want_exit = False
        self.message   = ""
        self.msg_color = 7

    def enter(self):
        self.want_exit = False
        self.message = ""

    def update(self):
        """Retourne True quand on veut quitter l'écran."""
        if pyxel.btnp(pyxel.KEY_E):
            self.want_exit = True

        if self.want_exit:
            self.want_exit = False
            return True

        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.inv.coins >= PACK_COST:
                self.inv.coins -= PACK_COST
                self._open_pack()
            else:
                self.message= f"Pas assez ! ({self.inv.coins}/{PACK_COST})"
                self.msg_color = 8

        return False

    def _open_pack(self):
        roll = random.random()
        if roll < 0.15:
            self.inv.speed_boost += 1
            self.message   = f"BOOST VITESSE x{self.inv.speed_boost} !"
            self.msg_color = 9
        elif roll < 0.20:
            self.inv.lava_slow += 1
            self.message   = f"LAVE RALENTIE x{self.inv.lava_slow} !"
            self.msg_color = 14
        else:
            old = self.inv.player_color
            choices = [c for c in PLAYER_COLORS if c != old]
            self.inv.player_color = random.choice(choices)
            self.message   = "NOUVELLE COULEUR !"
            self.msg_color = self.inv.player_color

    def draw(self):
        pyxel.cls(1)
        pyxel.text(52, 6, "=== PACKS ===", 10)
        pyxel.text(10, 18, f"Tes pieces : {self.inv.coins}", 10)
        pyxel.text(10, 26, f"Cout d'un pack : {PACK_COST}", 7)
        pyxel.line(10, 34, 150, 34, 5)
        pyxel.text(10, 38, "Contenu possible :", 7)
        pyxel.text(12, 47, "Boost vitesse  +15%  ->  20%", 9)
        pyxel.text(12, 55, "Lave ralentie  -20%  ->   10%", 14)
        pyxel.text(12, 63, "Couleur joueur       ->  70%", self.inv.player_color)
        pyxel.line(10, 72, 150, 72, 5)
        pyxel.text(10, 76, "Pouvoirs actifs :", 7)
        txt_spd  = f"SPD x{self.inv.speed_boost}"  if self.inv.speed_boost else "SPD : aucun"
        txt_slow = f"SLOW x{self.inv.lava_slow}"   if self.inv.lava_slow   else "SLOW: aucun"
        pyxel.text(12, 84, txt_spd,  9)
        pyxel.text(12, 92, txt_slow, 14)
        if self.message:
            bx = max(2, (SCREEN_WIDTH - len(self.message) * 4 - 4) // 2)
            pyxel.rectb(bx - 2, 100, len(self.message) * 4 + 6, 10, self.msg_color)
            pyxel.text(bx, 102, self.message, self.msg_color)
        pyxel.text(4,  112, "[ESPACE] Acheter", 10)
        pyxel.text(98, 112, "[E] Retour", 5)
        
class SimpleMenu:
    def __init__(self):
        self.options      = ["Play", "Packs"]
        self.selected     = 0
        self.active       = True
        self._block_enter = False
        pyxel.load("GRAPHI.pyxres")

    def reset(self):
        self.selected     = 0
        self.active       = True
        self._block_enter = True

    def update(self):
        if not self.active:
            return None
        if self._block_enter:
            if not pyxel.btn(pyxel.KEY_RETURN):
                self._block_enter = False
            return None
        if pyxel.btnp(pyxel.KEY_UP):
            self.selected = (self.selected - 1) % len(self.options)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.selected = (self.selected + 1) % len(self.options)
        elif pyxel.btnp(pyxel.KEY_RETURN):
            choice = self.options[self.selected]
            if choice == "Play":
                self.active = False
                return "play"
            elif choice == "Packs":
                return "packs"
        return None



    def draw(self, coins: int):
        pyxel.cls(0)
        pyxel.blt(45, 17, 0, 2, 81, 53, 27)
        pyxel.blt(45, 47, 0, 0, 0,  26,  8)
        pyxel.blt(46, 64, 0, 0, 16, 26,  8)
        pyxel.blt(103, 110, 0, 0, 65, 55, 8)
        pyxel.blt(4,   4,   0, 1, 32, 28, 20)
        for i in range(len(self.options)):
            color = pyxel.COLOR_LIGHT_BLUE if i == self.selected else pyxel.COLOR_BLACK
            pyxel.text(60, 50 + i * 15, "                   <==", color)
        pyxel.text(16, 8, f" {coins}", 10)



class Game:
    STATE_MENU    = "menu"
    STATE_PACKS   = "packs"
    STATE_PLAYING = "playing"
    STATE_WIN     = "win"
    WIN_DISPLAY_SECS = 2

    def __init__(self):
        pyxel.init(160, 120)
        self.inv   = Inventory()
        self.menu  = SimpleMenu()
        self.packs = PackScreen(self.inv)
        self.map   = MapManager(self.inv)
        self.state = self.STATE_MENU
        self.win_timer = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == self.STATE_MENU:
            action = self.menu.update()
            if action == "play":
                self._start_game()
            elif action == "packs":
                self.packs.enter()
                self.state = self.STATE_PACKS

        elif self.state == self.STATE_PACKS:
            if self.packs.update():
                self.state = self.STATE_MENU

        elif self.state == self.STATE_PLAYING:
            result = self.map.update()
            if result == "dead":
                self._go_to_menu()
            elif result == "win":
                self._show_win()

        elif self.state == self.STATE_WIN:
            if time.time() - self.win_timer >= self.WIN_DISPLAY_SECS:
                self._go_to_menu()

    def draw(self):
        if self.state == self.STATE_MENU:
            self.menu.draw(self.inv.coins)
        elif self.state == self.STATE_PACKS:
            self.packs.draw()
        elif self.state == self.STATE_PLAYING:
            self.map.draw()
        elif self.state == self.STATE_WIN:
            self._draw_win()

    def _start_game(self):
        self.map.current_level = 0
        self.map.load_level(0)
        self.state = self.STATE_PLAYING

    def _go_to_menu(self):
        self.menu.reset()
        self.state = self.STATE_MENU

    def _show_win(self):
        self.win_timer = time.time()
        self.state = self.STATE_WIN

    def _draw_win(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 1)
        msg = "TU AS GAGNE !"
        x = (SCREEN_WIDTH - len(msg) * 4) // 2
        pyxel.text(x,     52, msg, 10)
        pyxel.text(x - 1, 51, msg, 11)
        pyxel.text(30, 66, "Retour au menu...", 7)
        pyxel.text(50, 80, f"Pieces totales : {self.inv.coins}", 10)


Game()