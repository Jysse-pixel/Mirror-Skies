import pygame as p

p.init()
info = p.display.Info()

# Écran
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
MID_SCREEN_WIDTH = SCREEN_WIDTH // 2
MID_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

# Configuration Jeu
FPS = 60
PLAYER_SIZE = 50
SPEED = 5
SCROLL_BG_SPEED = -3
BULLET_SPEED = 10
GRAVITY = 0.25
MAX_FALL_SPEED = 0.5
JUMP_FORCE = -4

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)