import pygame as p
from settings import SCREEN_WIDTH, MID_SCREEN_HEIGHT

SCROLL_PLATFORMS_SPEED = -5 

class Level:
    def __init__(self):
        self.platforms = self._make_platforms()
    def _make_platforms(self):
        plats = [
            p.Rect(SCREEN_WIDTH//2, MID_SCREEN_HEIGHT - 100, 200, 50),
            p.Rect(SCREEN_WIDTH + 300, MID_SCREEN_HEIGHT - 150, 180, 40),
        ]
        return plats
    def update(self):

        for plat in list(self.platforms):
            plat.centerx += SCROLL_PLATFORMS_SPEED
            if plat.right < 0:
                self.platforms.remove(plat)
    def draw(self, screen, color=(0,255,0)):
        for plat in self.platforms:
            p.draw.rect(screen, color, plat)