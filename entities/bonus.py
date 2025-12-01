import pygame as p

class SpeedBonus:
    def __init__(self, x, y, size=20, color=(39, 101, 245)):
        self.rect = p.Rect(x, y, size, size)
        self.color = color

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)

    def apply_bonus(self):
        speed = 20

class InverseMalus:
    def __init__(self, x, y, size=20,color=(245,39,46)):
        self.rect = p.Rect(x, y, size, size)
        self.color = color
        

    def draw(self, screen):
        p.draw.rect(screen, self.rect,self.color)
