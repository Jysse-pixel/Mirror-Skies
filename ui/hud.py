import pygame as p

class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.hp = max_hp
        self.max_hp = max_hp
    def draw(self, surface):
        ratio = self.hp / self.max_hp
        p.draw.rect(surface, "red",   (self.x, self.y, self.w, self.h))
        p.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))