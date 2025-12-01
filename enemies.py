import pygame as p
import math
from entities.bullet import EnemyBullet
from settings import MID_SCREEN_HEIGHT

class TestEnemy: 
    def __init__(self, x, y, WIDTH, HEIGHT, HP, velocity_x, velocity_y, state:bool, color, mode="mobile"):
        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.HP = HP
        self.state = state
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.base_color = color          # couleur normale
        self.color = color               # couleur affichée
        self.flash_timer = 0             # durée du clignotement
        self.mode = mode                 #"mobile" ou "turret"
        self.rect = p.Rect(x, y, WIDTH, HEIGHT)
    
                # limites du mouvement vertical
        self.min_y = y - 50
        self.max_y = y + 50


    def move(self):
        # mouvement vertical
        #self.y += self.velocity_y
        #self.rect.y = self.y

        # rebond en haut/bas
        #if self.y <= self.min_y or self.y >= self.max_y:
            #self.velocity_y *= -1


        if self.mode == "mobile":
            self.y += self.velocity_y
            self.rect.y = self.y

        if self.y <= self.min_y or self.y >= self.max_y:
            self.velocity_y *= -1
        else:
            # mode tourelle : pas de mouvement
            pass

        
    def draw(self, screen):
        p.draw.rect(screen, self.color, self.rect)

    def hit(self):
        self.HP -= 1

        # Activer flash rouge pendant 3 frames
        self.flash_timer = 3
        self.color = (255, 0, 0)

        return self.HP <= 0
    
    def update_color(self):
        if self.flash_timer > 0:
            self.flash_timer -= 1

            # Quand le timer atteint zéro → retour à la couleur normale
            if self.flash_timer == 0:
                self.color = self.base_color
    
    def try_fire(self, player_rect, bullet_speed=8, fire_rate=60):
        if self.mode != "turret":
            return None  # ne tire pas si pas en mode tourelle

        # système de cooldown
        if not hasattr(self, "fire_cooldown"):
            self.fire_cooldown = 0

        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1
            return None

        self.fire_cooldown = fire_rate

        # direction vers le joueur
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)

        if dist == 0:
            return None

        vx = bullet_speed * dx / dist
        vy = bullet_speed * dy / dist

        return self.rect.centerx, self.rect.centery, vx, vy
