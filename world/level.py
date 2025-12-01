import pygame as p
from settings import SCREEN_WIDTH, MID_SCREEN_HEIGHT
from entities.platforms.plateforms import Destructible, Moving, Solid
from entities.coin import Coin
from entities.bonus import SpeedBonus


SCROLL_PLATFORMS_SPEED = -5 

class Level:
    def __init__(self):
        self.platforms = self._make_platforms()
        self.coins = self._make_coins()
        self.bonuses = self._make_bonuses()  

    def _make_platforms(self):
        base_x = SCREEN_WIDTH + 300
        plats = [
         
        ]
        return plats

    def _make_coins(self):
        base_x = SCREEN_WIDTH + 350
        coins = [
         
        ]
        return coins

    def _make_bonuses(self):
        base_x = SCREEN_WIDTH + 450
        bonuses = [
            SpeedBonus(base_x, 200),
        ]
        return bonuses

    def update(self):
        for plat in list(self.platforms):
            plat.update()
            plat.x += SCROLL_PLATFORMS_SPEED
            if plat.right < 0:
                self.platforms.remove(plat)

        for coin in list(self.coins):
            coin.update()
            coin.rect.x += SCROLL_PLATFORMS_SPEED
            if coin.rect.right < 0:
                self.coins.remove(coin)

        for bonus in list(self.bonuses):
            bonus.rect.x += SCROLL_PLATFORMS_SPEED
            if bonus.rect.right < 0:
                self.bonuses.remove(bonus)

    def draw(self, screen, color=(0,255,0)):
        for plat in self.platforms:
            c = getattr(plat, "color", color)
            p.draw.rect(screen, c, plat)

        for coin in self.coins:
            coin.draw(screen)

        for bonus in self.bonuses:
            bonus.draw(screen)