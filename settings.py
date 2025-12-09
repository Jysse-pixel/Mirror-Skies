import pygame as p


FPS = 60
PLAYER_SIZE = 50
SPEED = 5
SCROLL_BG_SPEED = -5
BULLET_SPEED = 10


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


p.init()
info = p.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
MID_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
MID_SCREEN_WIDTH = SCREEN_WIDTH // 2