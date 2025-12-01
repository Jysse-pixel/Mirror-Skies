import pygame as p

def fired(event):
    """Détecte si la touche de tir est pressée."""
    return event.type == p.KEYDOWN and event.key == p.K_SPACE