import pygame as p
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def check_collisions_and_bounds(rect, platforms, screen_w, screen_h):
    if rect.left < 0 or rect.right > screen_w:
        return False 
    if rect.top < 0 or rect.bottom > screen_h:
        return False

    for plat in platforms:
        if rect.colliderect(plat):
            return False 
            
    return True 