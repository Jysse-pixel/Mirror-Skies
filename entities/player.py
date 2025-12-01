import pygame as p
from settings import PLAYER_SIZE, SPEED, MID_SCREEN_HEIGHT


class Player(p.sprite.Sprite):
    def __init__(self, x, y, color=(255,0,0)):
        super().__init__()
        self.rect = p.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = color
        self.y = float(y)
        self.vy = 0.0

      
        self.speed = 5
        self.base_speed = self.speed
        self.speed_bonus_timer = 20

    def handle_input(self):
        k = p.key.get_pressed()
        if k[p.K_RIGHT]:
            self.rect.x += self.speed
        if k[p.K_LEFT]:
            self.rect.x -= self.speed
        if k[p.K_UP]:
            self.y -= 3
            self.vy = 0.0
        self.vy += 0.025
        self.y += self.vy
        self.rect.y = int(self.y)
        if self.rect.top < 0:
            self.rect.top = 0
            self.y = float(self.rect.y)
            self.vy = 0.0
        if self.rect.bottom > MID_SCREEN_HEIGHT:
            self.rect.bottom = MID_SCREEN_HEIGHT
            self.y = float(self.rect.y)
            self.vy = 0.0

    def mirror_rect(self, screen_h):
        return p.Rect(self.rect.x, (screen_h - self.rect.height) - self.rect.y, self.rect.width, self.rect.height)

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)

    def update(self, *args, **kwargs):
        self.handle_input()


        if self.speed_bonus_timer > 0:
            self.speed_bonus_timer -= 1
            if self.speed_bonus_timer <= 0:

                self.speed = self.base_speed