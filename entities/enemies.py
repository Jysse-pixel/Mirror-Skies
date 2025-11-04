import pygame as p
from settings import MID_SCREEN_HEIGHT

class TestEnemy: 
    def __init__(self, x, y, WIDTH, HEIGHT, HP, state:bool, color):
        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.HP = HP
        self.state = state
        self.color = color      # Couleur rose  : state = innactive
                                # Couleur jaune : state = active
        self.rect = p.Rect(x, y, WIDTH, HEIGHT)

        self.velocity_x = 5
    
    # def move(self, velocity_x):
        # Mouvements axe x
        # velocity_x += velocity_x
        
    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)