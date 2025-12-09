import pygame as p
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def check_player_and_bounds(player_rect: p.Rect, platforms, health_bar) -> bool:
    # réduction des hp
    for plat in platforms:
        if player_rect.colliderect(plat):
            health_bar.hp -= 1
    if health_bar.hp < 0:
        return False
    # bords d'écran
    if (player_rect.top <= 0 or player_rect.bottom >= SCREEN_HEIGHT or
        player_rect.left <= 0 or player_rect.right >= SCREEN_WIDTH):
        return False
    return True