import pygame as p
import math
from settings import MID_SCREEN_HEIGHT

class TestEnemy: 
    def __init__(self, x, y, w, h, hp, vy, color, mode="mobile"):
        self.rect = p.Rect(x, y, w, h)
        self.x_float = float(x)
        self.y_float = float(y)
        self.hp = hp
        self.color = color # couleur affichée
        self.base_color = color # couleur normale
        self.mode = mode #"mobile" ou "turret"
        # A changer car problème / A.A
        
        self.velocity_y = vy
        # limites du mouvement vertical
        self.min_y = y - 80
        self.max_y = y + 80
        
        self.flash_timer = 0 # durée du clignotement
        self.fire_cooldown = 0

    def update(self, scroll_speed):
        self.x_float += scroll_speed
        self.rect.x = int(self.x_float)

        if self.mode == "mobile":
            self.y_float += self.velocity_y
            self.rect.y = int(self.y_float)
            
            if self.y_float <= self.min_y or self.y_float >= self.max_y:
                self.velocity_y *= -1

        if self.flash_timer > 0:
            self.flash_timer -= 1
            if self.flash_timer == 0:
                self.color = self.base_color

    def hit(self):
        self.hp -= 1
        self.flash_timer = 3
        self.color = (255, 0, 0) # Flash blanc quand ennemie touché
        return self.hp <= 0

    def try_fire(self, target_rect, bullet_speed=7):
        if self.mode != "turret" and self.mode != "mobile":
            return None

        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1
            return None

        # Direction vers le joueur
        dx = target_rect.centerx - self.rect.centerx
        dy = target_rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)
        
        # Tirer seulement si le joueur est devant (à gauche) et à portée raisonnable
        if dist < 800 and dx < 0: 
            self.fire_cooldown = 90 # Cadence de tir
            vx = bullet_speed * dx / dist
            vy = bullet_speed * dy / dist
            return (self.rect.centerx, self.rect.centery, vx, vy)
        
        return None

    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)