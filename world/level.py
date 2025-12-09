import pygame as p
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, MID_SCREEN_HEIGHT, SCROLL_BG_SPEED
from entities.platforms.plateforms import Solid, Destructible, Moving
from entities.coin import Coin
from entities.bonus import SpeedBonus
from entities.enemies import TestEnemy

class Level:
    def __init__(self, level_number=1):
        self.platforms = []
        self.coins = []
        self.bonuses = []
        self.enemies = []
        
        self.level_number = level_number
        self.load_level(self.level_number)

    def load_level(self, level_number):
        """Charge le contenu du niveau spécifié."""
        if level_number == 1:
            self._generate_level_1()
        elif level_number == 2:
            # a faire plus tard
            pass
        else:
            # Si pas encore le niveau
            self._generate_level_1()

    def _generate_level_1(self):
        """Niveau 1 : Complet avec obstacles pour les DEUX joueurs"""
        
        self.platforms.append(Solid(SCREEN_WIDTH + 200, MID_SCREEN_HEIGHT - 50, 200, 30))
        self.platforms.append(Solid(SCREEN_WIDTH + 600, MID_SCREEN_HEIGHT - 120, 200, 30))
        self.coins.append(Coin(SCREEN_WIDTH + 650, MID_SCREEN_HEIGHT - 170))
        
        self.platforms.append(Solid(SCREEN_WIDTH + 400, SCREEN_HEIGHT - 100, 200, 30))
        self.coins.append(Coin(SCREEN_WIDTH + 450, SCREEN_HEIGHT - 150))
        self.enemies.append(TestEnemy(SCREEN_WIDTH + 800, SCREEN_HEIGHT - 100, 50, 50, 2, 0, (200, 150, 60), "turret"))

        start_wall_x = SCREEN_WIDTH + 1200
        for i in range(3):
            self.platforms.append(Destructible(start_wall_x, MID_SCREEN_HEIGHT - 50 - (i * 60), 50, 50))
        self.enemies.append(TestEnemy(start_wall_x + 300, MID_SCREEN_HEIGHT - 100, 60, 60, 3, 0, (200, 150, 60), "turret"))

        for i in range(3):
             self.platforms.append(Destructible(start_wall_x, SCREEN_HEIGHT - 50 - (i * 60), 50, 50))
        self.enemies.append(TestEnemy(start_wall_x + 400, SCREEN_HEIGHT - 200, 60, 60, 3, 0, (200, 150, 60), "turret"))

        self.platforms.append(Moving(SCREEN_WIDTH + 1800, MID_SCREEN_HEIGHT - 100, 150, 30, color=(255, 100, 100), min_y=MID_SCREEN_HEIGHT - 200, max_y=MID_SCREEN_HEIGHT - 50, speed=2.0))
        self.enemies.append(TestEnemy(SCREEN_WIDTH + 2200, MID_SCREEN_HEIGHT - 150, 50, 50, 2, 2.5, (150, 0, 150), "mobile"))

        self.platforms.append(Moving(SCREEN_WIDTH + 1900, SCREEN_HEIGHT - 150, 150, 30, color=(255, 100, 100), min_y=SCREEN_HEIGHT - 250, max_y=SCREEN_HEIGHT - 100, speed=3.0))
        self.enemies.append(TestEnemy(SCREEN_WIDTH + 2300, SCREEN_HEIGHT - 150, 50, 50, 2, -2.5, (150, 0, 150), "mobile"))

        tunnel_x = SCREEN_WIDTH + 3000
        
        self.platforms.append(Solid(tunnel_x, 50, 300, 40)) 
        self.platforms.append(Solid(tunnel_x, MID_SCREEN_HEIGHT - 40, 300, 40)) 
        self.coins.append(Coin(tunnel_x + 150, MID_SCREEN_HEIGHT // 2))

        self.platforms.append(Solid(tunnel_x, MID_SCREEN_HEIGHT + 40, 300, 40))
        self.platforms.append(Solid(tunnel_x, SCREEN_HEIGHT - 50, 300, 40))
        self.coins.append(Coin(tunnel_x + 150, MID_SCREEN_HEIGHT + 150))

        self.platforms.append(Destructible(SCREEN_WIDTH + 3800, MID_SCREEN_HEIGHT // 2, 60, 60))
        self.bonuses.append(SpeedBonus(SCREEN_WIDTH + 3900, MID_SCREEN_HEIGHT // 2))
        
        self.platforms.append(Solid(SCREEN_WIDTH + 4500, MID_SCREEN_HEIGHT - 80, 150, 30))
        self.enemies.append(TestEnemy(SCREEN_WIDTH + 4520, MID_SCREEN_HEIGHT - 140, 50, 50, 5, 0, (200, 50, 50), "turret"))
        
        self.enemies.append(TestEnemy(SCREEN_WIDTH + 3800, SCREEN_HEIGHT - 150, 60, 60, 3, 0, (200, 50, 50), "turret"))
        self.platforms.append(Solid(SCREEN_WIDTH + 4600, SCREEN_HEIGHT - 150, 150, 30))
        self.enemies.append(TestEnemy(SCREEN_WIDTH + 4620, SCREEN_HEIGHT - 210, 50, 50, 5, 0, (200, 50, 50), "turret"))


        for i in range(5):
            self.coins.append(Coin(SCREEN_WIDTH + 5200 + (i * 60), MID_SCREEN_HEIGHT // 2)) # Haut
            self.coins.append(Coin(SCREEN_WIDTH + 5200 + (i * 60), SCREEN_HEIGHT - 150))   # Bas

    # Hania tu peux faire le prochain niveau avec la même logique que en haut
    # def _generate_level_2(self):
    
    def update(self):
        
        for plat in list(self.platforms):
            plat.update(SCROLL_BG_SPEED)
            if plat.right < 0: self.platforms.remove(plat)

        for coin in list(self.coins):
            coin.update(SCROLL_BG_SPEED)
            if coin.rect.right < 0: self.coins.remove(coin)

        for bonus in list(self.bonuses):
            bonus.update(SCROLL_BG_SPEED)
            if bonus.rect.right < 0: self.bonuses.remove(bonus)

        for enemy in list(self.enemies):
            enemy.update(SCROLL_BG_SPEED)
            if enemy.rect.right < 0: self.enemies.remove(enemy)

    def draw(self, screen):
        for plat in self.platforms:
            plat.draw(screen)
        for coin in self.coins:
            coin.draw(screen)
        for bonus in self.bonuses:
            bonus.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)