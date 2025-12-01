import pygame as p
from settings import BULLET_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

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

class EnemyBullet:
    def __init__(self, x, y, vx, vy, size=8, color=(255,80,80)):
        self.rect = p.Rect(x, y, size, size)
        self.vx = vx
        self.vy = vy
        self.color = color

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def offscreen(self):
        return (self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or
                self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT)

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)
