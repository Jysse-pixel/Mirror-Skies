import pygame as p
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCROLL_BG_SPEED

class Background:
    def __init__(self, path: str):
        self.image = p.image.load(path).convert()
        self.image = p.transform.smoothscale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.scroll = 0
        self.w = self.image.get_width()
        self.tiles = (SCREEN_WIDTH // self.w) + 2

    def update(self):
        self.scroll += SCROLL_BG_SPEED
        if abs(self.scroll) > self.w:
            self.scroll = 0

    def draw(self, screen):
        for i in range(self.tiles):
            x = i * self.w + self.scroll
            screen.blit(self.image, (x, 0))