import pygame as p

class Coin:
    def __init__(self, x, y, size=20, color=(255, 215, 0)):
        self.rect = p.Rect(x, y, size, size)
        self.color = color
        self.dy = 0.5
        self.min_y = y - 15
        self.max_y = y + 15
        self.direction = 1

    def update(self):
        self.rect.y += self.dy * self.direction
        if self.rect.y <= self.min_y:
            self.rect.y = self.min_y
            self.direction = 1
        if self.rect.y >= self.max_y:
            self.rect.y = self.max_y
            self.direction = -1

    def draw(self, screen):
        p.draw.ellipse(screen, self.color, self.rect)