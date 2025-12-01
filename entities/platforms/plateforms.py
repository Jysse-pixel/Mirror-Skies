import pygame as p
from typing import Tuple

class Platform(p.Rect):
    def __init__(self, x: int, y: int, w: int = 200, h: int = 50, color: Tuple[int,int,int]=(100,100,100)):
        p.Rect.__init__(self, x, y, w, h)
        self._y = float(y)
        self.color = color
        self.alive = True
        self.destructible = False

    def update(self, dt: float = 0):
        pass

    def draw(self, screen: p.Surface):
        p.draw.rect(screen, self.color, self)

    def on_collide(self, other):
        pass

class Solid(Platform):
    def __init__(self, x, y, w=200, h=50, color=(100,100,100)):
        super().__init__(x, y, w, h, color)

class Destructible(Platform):
    def __init__(self, x, y, w=200, h=50, color=(0,200,0)):
        super().__init__(x, y, w, h, color)
        self.destructible = True

    def update(self, dt: float = 0):
        pass

    def draw(self, screen: p.Surface):
        ratio = max(0.0, min(1.0, self.health / self.max_health))
        r = int(self.color[0] * ratio)
        g = int(self.color[1] * ratio)
        b = int(self.color[2] * ratio)
        p.draw.rect(screen, (r, g, b), self)

class Moving(Platform):
    def __init__(self, x, y, w=150, h=100, color=(255,0,0), min_y=None, max_y=None, speed: float = 0.5):
        super().__init__(x, y, w, h, color)
        self.min_y = (y - 20) if min_y is None else min_y
        self.max_y = (y + 20) if max_y is None else max_y
        self.speed = float(speed)
        self.direction = 1.0
        

    def update(self, dt: float = 0):
        self._y += self.speed * self.direction
        if self._y <= self.min_y:
            self._y = self.min_y
            self.direction = 1.0
        elif self._y >= self.max_y:
            self._y = self.max_y
            self.direction = -1.0
        self.y = int(self._y)