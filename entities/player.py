import pygame as p
from settings import PLAYER_SIZE, MID_SCREEN_HEIGHT, GRAVITY, JUMP_FORCE, SPEED, MAX_FALL_SPEED

class Player:
    def __init__(self, x, y, color=(255, 0, 0)):
        self.rect = p.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = color
        self.y_float = float(y)
        self.vy = 0.0
        
        self.base_speed = SPEED
        self.speed = SPEED
        self.bonus_timer = 0

    def handle_input(self):
        keys = p.key.get_pressed()
        
        if keys[p.K_RIGHT]:
            self.rect.x += self.speed
        if keys[p.K_LEFT]:
            self.rect.x -= self.speed
            
        if keys[p.K_UP]:
            self.vy += JUMP_FORCE * 0.2 
            if self.vy < JUMP_FORCE: 
                self.vy = JUMP_FORCE
        
        self.vy += GRAVITY
        
        if self.vy > MAX_FALL_SPEED:
            self.vy = MAX_FALL_SPEED
            
        self.y_float += self.vy
        
        # Limites
        self.rect.y = int(self.y_float)
        
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