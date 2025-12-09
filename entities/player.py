import pygame as p
from settings import PLAYER_SIZE, MID_SCREEN_HEIGHT, JUMP_FORCE, SPEED

class Player:
    def __init__(self, x, y, color=(255, 0, 0)):
        self.rect = p.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = color
        self.vy = 0.0
        
        self.base_speed = SPEED
        self.speed = SPEED
        self.bonus_timer = 0

    def handle_input(self):
        keys = p.key.get_pressed()
        
        if keys[p.K_RIGHT] or keys[p.K_d]:
            self.rect.x += self.speed

        if keys[p.K_LEFT] or keys[p.K_q]:
            self.rect.x -= self.speed
            
        if keys[p.K_UP] or keys[p.K_z]:
            self.rect.y -= self.speed
        
        if keys[p.K_DOWN] or keys[p.K_s]:
            self.rect.y += self.speed
        
        
        # Limites
        
        # Plafond
        if self.rect.top < 0:
            self.rect.top = 0
            self.y_float = 0
            self.vy = 0
            
        # Milieu de l'écran
        if self.rect.bottom > MID_SCREEN_HEIGHT:
            self.rect.bottom = MID_SCREEN_HEIGHT
            self.y_float = self.rect.y
            self.vy = 0

    def get_mirror_rect(self, screen_height):
        return p.Rect(self.rect.x, (screen_height - self.rect.height) - self.rect.y, self.rect.width, self.rect.height)

    def update(self):
        self.handle_input()
        
        if self.bonus_timer > 0:
            self.bonus_timer -= 1
            if self.bonus_timer <= 0:
                self.speed = self.base_speed
                self.color = (255, 0, 0)

    def activate_speed_bonus(self, duration=300):
        self.speed = self.base_speed * 2
        self.bonus_timer = duration
        self.color = (0, 100, 255) 

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)