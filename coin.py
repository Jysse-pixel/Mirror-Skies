import pygame as p
import math
from settings import *

class Coin:
    """Pièce à collecter qui rapporte 1 point"""
    
    def __init__(self, x, y, size=30):
        self.rect = p.Rect(x, y, size, size)
        self.size = size
        self.color = (255, 215, 0)  # Or
        self.outline_color = (218, 165, 32)  # Or foncé
        self.collected = False
        
        # Animation de rotation
        self.angle = 0
        self.rotation_speed = 3
        
    def update(self):
        """Met à jour l'animation de la pièce"""
        if not self.collected:
            self.angle = (self.angle + self.rotation_speed) % 360
    
    def draw(self, screen):
        """Dessine la pièce avec un effet de rotation"""
        if not self.collected:
            # Effet de rotation en modifiant la largeur
            width_factor = abs(math.cos(math.radians(self.angle)))
            current_width = int(self.size * width_factor)
            
            if current_width > 2:
                # Pièce
                coin_rect = p.Rect(
                    self.rect.centerx - current_width // 2,
                    self.rect.y,
                    current_width,
                    self.size
                )
                p.draw.ellipse(screen, self.color, coin_rect)
                p.draw.ellipse(screen, self.outline_color, coin_rect, 2)
                
                # Symbole au centre (quand la pièce est de face)
                if width_factor > 0.7:
                    symbol_size = int(self.size * 0.4)
                    symbol_rect = p.Rect(
                        self.rect.centerx - symbol_size // 2,
                        self.rect.centery - symbol_size // 2,
                        symbol_size,
                        symbol_size
                    )
                    p.draw.circle(screen, self.outline_color, 
                                (symbol_rect.centerx, symbol_rect.centery), 
                                symbol_size // 2, 2)
    
    @staticmethod
    def draw_all(screen, coins):
        """Dessine toutes les pièces de la liste"""
        for coin in coins:
            coin.draw(screen)