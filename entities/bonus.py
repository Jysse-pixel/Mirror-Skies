import pygame as p

class SpeedBonus:
    def __init__(self, x, y, size=30):
        self.rect = p.Rect(x, y, size, size)
        self.x_float = float(x)
        self.color = (0, 100, 255)
        self.type = "speed"

    def update(self, scroll_speed):
        self.x_float += scroll_speed
        self.rect.x = int(self.x_float)

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)