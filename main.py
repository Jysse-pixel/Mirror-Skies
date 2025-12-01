import pygame as p
from core.game import Game
from ui.menu import start_menu

if __name__ == "__main__":
    p.init()
    start_menu()
    Game().run() 
    p.quit()