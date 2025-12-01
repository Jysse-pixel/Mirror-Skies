import pygame as p

class Platform(p.Rect):
    def __init__(self, x, y, w=200, h=50, color=(100, 100, 100)):
        super().__init__(x, y, w, h)
        self.x_float = float(x)
        self.color = color
        self.destructible = False

    def update(self, scroll_speed):
        self.x_float += scroll_speed
        self.x = int(self.x_float)

    def draw(self, screen):
        p.draw.rect(screen, self.color, self)

class Solid(Platform):
    pass

class Destructible(Platform):
    def __init__(self, x, y, w=200, h=50, color=(0, 200, 0)):
        super().__init__(x, y, w, h, color)
        self.destructible = True
        self.health = 3   
        self.max_health = 3

    def take_damage(self):
        self.health -= 1
        return self.health <= 0

    def draw(self, screen):
        ratio = max(0, self.health / self.max_health)
        r = int(self.color[0] * ratio)
        g = int(self.color[1] * ratio)
        b = int(self.color[2] * ratio)
        p.draw.rect(screen, (255, 255, 255), self, 2)

class Moving(Platform):
    def __init__(self, x, y, w=150, h=30, color=(255, 0, 0), min_y=None, max_y=None, speed=2.0):
        super().__init__(x, y, w, h, color)
        self.min_y = (y - 50) if min_y is None else min_y
        self.max_y = (y + 50) if max_y is None else max_y
        self.vertical_speed = float(speed)
        self.direction = 1.0
        self.y_float = float(y) 

    def update(self, scroll_speed):
        super().update(scroll_speed)

        self.y_float += self.vertical_speed * self.direction

        if self.y_float <= self.min_y:
            self.y_float = self.min_y
            self.direction = 1.0
        elif self.y_float >= self.max_y:
            self.y_float = self.max_y
            self.direction = -1.0
            
        self.y = int(self.y_float)