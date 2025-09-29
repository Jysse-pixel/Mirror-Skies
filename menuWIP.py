from time import sleep
import pygame
import pygame_menu as pm
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((600,400))

mainmenu = pm.Menu('Bienvenu', 600, 400,
                   theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button