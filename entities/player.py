import pygame as p
from settings import PLAYER_SIZE, SPEED, MID_SCREEN_HEIGHT

class Player:
    def __init__(self, x, y, color=(255,0,0)):
        self.rect = p.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = color
    def handle_input(self):
        k = p.key.get_pressed()
        if k[p.K_DOWN]:  
            self.rect.y += SPEED
        if k[p.K_UP]:    
            self.rect.y -= SPEED
        if k[p.K_RIGHT]: 
            self.rect.x += SPEED
        if k[p.K_LEFT]:  
            self.rect.x -= SPEED
        self.rect.y = max(0, min(self.rect.y, MID_SCREEN_HEIGHT - self.rect.height))
    def mirror_rect(self, screen_h):
        return p.Rect(self.rect.x, (screen_h - self.rect.height) - self.rect.y, self.rect.width, self.rect.height)
    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)