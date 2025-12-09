import pygame as p
from core.game import Game
from ui.menu import start_menu

if __name__ == "__main__":
    p.init()
    action = start_menu()

    if action == "play":
        Game().run() 
    elif action == "quit":
        p.quit()