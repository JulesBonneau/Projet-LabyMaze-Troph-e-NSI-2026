import pyxel
import random
import time

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
LAVA_SPEED = 1

class MapManager:
    def __init__(self):
        self.player_x = 80
        self.player_y = 118
        self.player_w = 4
        self.player_h = 4
        self.lava_y = SCREEN_HEIGHT 
        self.player_speed = 1.46

        
        self.rectangles = [
            (0, 0, 2, 120),    
            (158, 0, 2, 120),  
            (0, 0, 132, 2),     
            (0, 118, 160, 2),
        
            (0, 99, 140, 2),
            (150, 99, 10, 2),
            (20, 83, 170, 2),
            (0, 83, 10, 2),
            (0, 67, 115, 2),
            (130, 67, 40, 2),
            (15, 51, 150, 2),
            (0, 35, 40, 2),
            (55, 35, 160, 2),
            (0, 22, 150, 2),
            (7, 11, 151, 2),
            (149, 0, 10, 2)
                
            
        
        ]
        
    
    def update(self):
        if self.lava_y > 1:
            self.lava_y -= 0.08
            
        
        if self.player_y + self.player_h > self.lava_y:
            self.reset_player()
            self.die_player()
        
        
        if self.player_y < -2 and self.player_x <149:
            self.reset_player()
            self.lava_y = SCREEN_HEIGHT
            self.rectangles= [
                (0, 0, 2, 120),    
                (158, 0, 2, 120),  
                (0, 0, 149, 2),     
                (0, 118, 160, 2),
                
                (0, 105, 13, 2),
                (13, 77, 2, 30),
                (0, 68, 90, 2),
                (23, 68, 2, 39),
                (35, 95, 2, 12),
                (35, 95, 65, 2),
                (90, 68, 2, 17),
                (35, 85, 57, 2),
                (35, 77, 2, 8),
                (35, 77, 45, 2),
                (100, 50, 2, 56),
                (47, 105, 100, 2),
                (13, 58, 79, 2),
                (13, 40, 2, 18),
                (13, 40, 30, 2),
                (43, 50, 57, 2),
                (43, 40, 2, 10),
                (28, 51, 2, 7),
                (22, 51, 6, 2),
                (13, 13, 2, 15),
                (13, 13, 20, 2),
                (13, 28, 89, 2),
                (43, 0, 2, 30),
                (58, 13, 42, 2),
                (100, 13, 2, 17),
                (120, 0, 2, 42),
                (56, 40, 66, 2),
                (149, 0, 2, 42),
                (135, 17, 14, 2),
                (135, 17, 2, 15),
                (135, 42, 16, 2),
                (135, 42, 2, 25),
                (121, 67, 16, 2),
                (121, 50, 2, 18),
                (147, 52, 2, 55),
                (147, 52, 11, 2),
                (110, 78, 18, 2),
                (128, 78, 2, 12),
                (128, 90, 20, 2),
                (133, 90, 2, 7),
                (133, 97, 8, 2)
                
                
        ]
        
        if self.player_y < -2 and self.player_x >149:
            self.reset_player()
            self.lava_y = SCREEN_HEIGHT
            if self.lava_y > 1:
                self.lava_y -= 0.5
            self.rectangles= [
                (0, 0, 2, 120),    
                (158, 0, 2, 120),  
                (0, 0, 150, 2),     
                (0, 118, 160, 2),
                
                (11, 84, 2, 34),
                (22, 67, 2, 51),
                (11, 67, 22, 2),
                (33, 67, 2, 34),
                (22, 19, 2, 34),
                (11, 51, 23, 2),
                (2, 34, 11, 2),
                (11, 17, 22, 2),
                (33, 17, 2, 17),
                (33, 34, 44, 2),
                (44, 2, 2, 34),
                (33, 85, 35, 2),
                (44, 101, 2, 17),
                (55, 86, 2, 17),
                (55, 34, 2, 17),
                (44, 51, 13, 2),
                (44, 51, 2, 17),
                (44, 68, 24, 2),
                (55, 17, 79, 2),
                (77, 34, 2, 35),
                (66, 51, 11, 2),
                (77, 68, 13, 2),
                (88, 68, 2, 17),
                (77, 85, 13, 2),
                (66, 101, 2, 17),
                (66, 101, 24, 2),
                (99, 68, 12, 2),
                (99, 68, 2, 34),
                (99, 101, 23, 2),
                (110, 101, 2, 17),
                (88, 17, 2, 35),
                (88, 51, 23, 2),
                (109, 34, 2, 17),
                (109, 68, 2, 17),
                (99, 34, 23, 2),
                (109, 2, 2, 17),
                (132, 17, 2, 51),
                (121, 68, 13, 2),
                (121, 51, 2, 17),
                (132, 34, 16, 2),
                (121, 85, 13, 2),
                (132, 85, 2, 18),
                (132, 101, 34, 2),
                (148, 2, 2, 17),
                (148, 51, 14, 2),
                (148, 51, 2, 19),
                (148, 85, 17, 2),
                (148, 101, 2, 17)
                
                
                
                
                
        ]
                
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            if not self.check_collision(self.player_x - self.player_speed, self.player_y):
                self.player_x -= self.player_speed

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            if not self.check_collision(self.player_x + self.player_speed, self.player_y):
                self.player_x += self.player_speed

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            if not self.check_collision(self.player_x, self.player_y - self.player_speed):
                self.player_y -= self.player_speed

        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            if not self.check_collision(self.player_x, self.player_y + self.player_speed):
                self.player_y += self.player_speed

        self.player_x = max(2, min(self.player_x, SCREEN_WIDTH - self.player_w -2))
        
    def check_collision(self, x, y):
        for rx, ry, rw, rh in self.rectangles:
            if (x + self.player_w > rx and x < rx + rw and
                y + self.player_h > ry and y < ry + rh):
                return True  
        return False

    def reset_player(self):
        self.player_x = 14
        self.player_y = 111
        self.lava_y = SCREEN_HEIGHT
        
    def die_player(self):
        SimpleMenu()
            
        

    def draw(self):
        pyxel.cls(0) 
        for rx, ry, rw, rh in self.rectangles:
            pyxel.rect(rx, ry, rw, rh, 5) 
        pyxel.rect(0, self.lava_y, 160, SCREEN_HEIGHT - self.lava_y, 8)
        pyxel.rect(self.player_x, self.player_y, self.player_w, self.player_h, 11)

class SimpleMenu:
    def __init__(self):
        self.options = ["Play","Packs"]
        self.selected = 0
        self.active = True
        self.message = ""  # Message to display for actions
        pyxel.load("GRAPHI.pyxres")
    def update(self):
        if not self.active:
            return

        # Navigate menu with UP and DOWN arrows
        if pyxel.btnp(pyxel.KEY_UP):
            self.selected = (self.selected - 1) % len(self.options)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.selected = (self.selected + 1) % len(self.options)
        elif pyxel.btnp(pyxel.KEY_RETURN):
            choice = self.options[self.selected]
            print(choice)
            if choice == "Play":
                pyxel.cls(0)
                self.active = False
            elif choice == "Packs":
                pyxel.cls(0)
                self.message = f"Random number: {random.randint(1, 10)}"

    def draw(self):
      
        pyxel.cls(0)  # Clear screen      
        pyxel.blt(45, 17,0, 2, 81, 53, 27)# logo
        pyxel.blt(45, 47,0, 0, 0, 26, 8)# play
        pyxel.blt(46, 64,0, 0, 16, 26, 8) # pack
        pyxel.blt(103, 110,0, 0, 65, 55, 8)# made by
        pyxel.blt(4, 4,0, 1,32, 28, 20) # COINCOIN

        # Draw menu options
        for i, option in enumerate(self.options):
            color = pyxel.COLOR_LIGHT_BLUE if i == self.selected else pyxel.COLOR_BLACK
            pyxel.text(60, 50 + i * 15, "                   <==", color)

        # Draw the action message below menu
        if self.message:
            pyxel.text(40, 90, self.message, pyxel.COLOR_PURPLE)
        

class Game:
    def __init__(self):
        pyxel.init(160, 120)
        self.menu = SimpleMenu()
        self.map = MapManager()
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.menu.active:
            self.menu.update()
        else:
            self.map.update()

    def draw(self):
        if self.menu.active:
            self.menu.draw()
        else:
            self.map.draw()

# Run the simple menu game
Game()