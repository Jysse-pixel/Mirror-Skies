import pygame as p
import math

class Coin:
    def __init__(self, x, y, size=30):
        self.rect = p.Rect(x, y, size, size)
        self.size = size
        self.x_float = float(x)
        self.color = (255, 215, 0)
        self.outline_color = (218, 165, 32)
        
        # Animation
        self.angle = 0
        self.rotation_speed = 3

    def update(self, scroll_speed):
        self.x_float += scroll_speed
        self.rect.x = int(self.x_float)
        self.angle = (self.angle + self.rotation_speed) % 360

    def draw(self, screen):
        # Rotation
        width_factor = abs(math.cos(math.radians(self.angle)))
        current_width = int(self.size * width_factor)
        
        if current_width > 2:
            coin_rect = p.Rect(
                self.rect.centerx - current_width // 2,
                self.rect.y,
                current_width,
                self.size
            )
            p.draw.ellipse(screen, self.color, coin_rect)
            p.draw.ellipse(screen, self.outline_color, coin_rect, 2)