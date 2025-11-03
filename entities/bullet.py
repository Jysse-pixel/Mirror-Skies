import pygame as p
from settings import BULLET_SPEED, SCREEN_WIDTH

class Bullet:
    def __init__(self, x, y, w=15, h=5, color=(255,255,0)):
        self.rect = p.Rect(x, y, w, h)
        self.color = color
    def update(self):
        self.rect.x += BULLET_SPEED
    def offscreen(self):
        return self.rect.left > SCREEN_WIDTH
    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)