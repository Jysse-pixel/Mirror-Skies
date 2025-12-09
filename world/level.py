import pygame as p
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, MID_SCREEN_HEIGHT, SCROLL_BG_SPEED
from entities.platforms.plateforms import Solid, Destructible, Moving
from entities.coin import Coin
from entities.bonus import SpeedBonus
from entities.enemies import Enemy

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
        current_x = SCREEN_WIDTH + 50

        # Pièces
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 100))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 100))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 150))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 150))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 200))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 200))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 250))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 250))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 300))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 300))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 300))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 300))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 300))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 300))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 250))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 250))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 200))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 200))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 150))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 150))

        current_x += 100

        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + 100))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT - 100))


        # Deux mures destructibles et un enemi
        current_x += 200

        wall_y_top = (MID_SCREEN_HEIGHT // 2) - 50
        self.platforms.append(Destructible(current_x, wall_y_top, 50, 100))
        
        wall_y_bot = MID_SCREEN_HEIGHT + (MID_SCREEN_HEIGHT // 2) - 50
        self.platforms.append(Destructible(current_x, wall_y_bot, 50, 100))

        self.enemies.append(Enemy(current_x - 300, wall_y_top, 40, 40, 3, 2, (200, 0, 0), mode="mobile"))


        current_x += 600
        
        # Tunnel étroit
        
        center_a = MID_SCREEN_HEIGHT // 2
        ceil_h_a = center_a - (60 // 2)
        floor_y_a = center_a + (60 // 2)
        floor_h_a = MID_SCREEN_HEIGHT - floor_y_a
        
        self.platforms.append(Solid(current_x, 0, 1000, ceil_h_a, (50, 50, 50))) 

        self.platforms.append(Solid(current_x, floor_y_a, 1000, floor_h_a, (50, 50, 50)))

        center_b = MID_SCREEN_HEIGHT + (MID_SCREEN_HEIGHT // 2)
        ceil_h_b = (center_b - MID_SCREEN_HEIGHT) - (60 // 2)
        floor_y_b = center_b + (60 // 2)
        floor_h_b = SCREEN_HEIGHT - floor_y_b
        
        self.platforms.append(Solid(current_x, MID_SCREEN_HEIGHT, 1000, ceil_h_b, (50, 50, 50))) 

        self.platforms.append(Solid(current_x, floor_y_b, 1000, floor_h_b, (50, 50, 50)))

        bonus_x = current_x + (1000 // 2)
        self.bonuses.append(SpeedBonus(bonus_x, center_a - 15))


        current_x += 1300

        # Deux plateformes devant l'entrée

        self.platforms.append(Moving(current_x, (MID_SCREEN_HEIGHT // 2), 150, 30, color=(255, 100, 0), min_y=(MID_SCREEN_HEIGHT // 2) - 150, max_y=(MID_SCREEN_HEIGHT // 2) + 150, speed=4.0))

        self.platforms.append(Moving(current_x, MID_SCREEN_HEIGHT + (MID_SCREEN_HEIGHT // 2), 150, 30, color=(255, 100, 0), min_y=MID_SCREEN_HEIGHT + (MID_SCREEN_HEIGHT // 2) - 150, max_y=MID_SCREEN_HEIGHT + (MID_SCREEN_HEIGHT // 2) + 150, speed=4.0))

        current_x += 300
        self.enemies.append(Enemy(current_x,MID_SCREEN_HEIGHT + 200,40,40,1,0,color=(200, 0, 0),mode="turret"))
        self.enemies.append(Enemy(current_x,MID_SCREEN_HEIGHT - 200,40,40,1,0,color=(200, 0, 0),mode="turret"))

        current_x += 400
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT // 2))
        self.coins.append(Coin(current_x, MID_SCREEN_HEIGHT + MID_SCREEN_HEIGHT // 2))

    
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