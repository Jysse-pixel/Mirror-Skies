import pygame as p

def fired(event):
    return event.type == p.KEYDOWN and event.key == p.K_SPACE