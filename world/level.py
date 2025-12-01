import pygame as p
import random
from settings import SCREEN_WIDTH, MID_SCREEN_HEIGHT, SCROLL_BG_SPEED
from entities.platforms.plateforms import Solid, Destructible
from entities.coin import Coin
from entities.bonus import SpeedBonus
from entities.enemies import TestEnemy

class Level:
    def __init__(self):
        self.platforms = []
        self.coins = []
        self.bonuses = []
        self.enemies = []
        
        self._generate_level()

    def _generate_level(self):

        self.platforms.append(Solid(SCREEN_WIDTH + 200, MID_SCREEN_HEIGHT - 100, 200, 30))
        self.platforms.append(Solid(SCREEN_WIDTH + 600, MID_SCREEN_HEIGHT - 150, 200, 30))
        

        self.enemies.append(TestEnemy(SCREEN_WIDTH + 1100, MID_SCREEN_HEIGHT - 100, 60, 60, 5, 0, (200, 150, 60), "turret"))

        coin_positions = [
            (SCREEN_WIDTH + 250, MID_SCREEN_HEIGHT - 150),
            (SCREEN_WIDTH + 300, MID_SCREEN_HEIGHT - 170),
            (SCREEN_WIDTH + 650, MID_SCREEN_HEIGHT - 200),
            (SCREEN_WIDTH + 1000, 100)
        ]
        for pos in coin_positions:
            self.coins.append(Coin(pos[0], pos[1]))

        self.bonuses.append(SpeedBonus(SCREEN_WIDTH + 1200, 200))

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