import pygame as p

class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        self.rect = p.Rect(x, y, w, h)
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = max(0, self.hp / self.max_hp)
        
        p.draw.rect(surface, "red", self.rect)
        
        green_width = int(self.rect.width * ratio)
        if green_width > 0:
            green_rect = p.Rect(self.rect.x, self.rect.y, green_width, self.rect.height)
            p.draw.rect(surface, "green", green_rect)