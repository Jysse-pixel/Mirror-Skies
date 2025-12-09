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

def check_player_and_enemy(player_rect: p.Rect, enemy, health_bar) -> bool:
    # Collision joueur / ennemi
    if player_rect.colliderect(enemy.rect):
        health_bar.hp -= 1

    if health_bar.hp < 0:
        return False

    return True


def check_coin_collection(coins: list, player_rect: p.Rect) -> int:
    """
    Vérifie si le joueur collecte des pièces.
    
    Args:
        coins: Liste des pièces dans le niveau
        player_rect: Rectangle du joueur
        
    Returns:
        Nombre de points collectés (nombre de pièces ramassées)
    """
    points_gained = 0
    
    for coin in coins:
        if not coin.collected and coin.rect.colliderect(player_rect):
            coin.collected = True
            points_gained += 1
    
    return points_gained