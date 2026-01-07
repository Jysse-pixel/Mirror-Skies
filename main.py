import pygame as p
from core.game import Game
from ui.menu import start_menu, level_choice

if __name__ == "__main__":
    p.init()
    action = start_menu()

    if action == "quit":
        p.quit()
    elif action == "level_choice":
        level_selected = level_choice()
        if level_selected != "back":
            Game(level_selected).run()
        elif level_selected == "back":
            action = start_menu