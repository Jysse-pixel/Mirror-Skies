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
            self._generate_level_1()

    def _generate_level_1(self):
            """Niveau 1"""
    
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