import pygame as p
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

## Couleurs
WHITE = (255, 255, 255)
TRANSLUCENT_BLUE = (0,80,200,180)
HOVER_BLUE = (0, 140, 255, 220)
SHADOW = (0, 0, 0)
    
## Polices
try:
    FONT_TITLE = p.font.Font("assets/Jersey10-Regular.ttf", 96)
    FONT_BUTTON = p.font.Font("assets/Doto-Regular.ttf", 40)
except:
    FONT_TITLE = p.font.SysFont(None, 72)
    FONT_BUTTON = p.font.SysFont(None, 40)


class Button:
    def __init__(self, text, center_y, action):
        self.text = text
        self.center_y=center_y
        self.action = action
        self.width, self.height = 300, 60
        self.rect = p.Rect((0, 0, self.width, self.height))
        self.rect.center = (SCREEN_WIDTH // 2, center_y)

    def draw(self, win, mouse_pos):
        is_hover = self.rect.collidepoint(mouse_pos)
        color = HOVER_BLUE if is_hover else TRANSLUCENT_BLUE
        button_surface = p.Surface((self.width, self.height),p.SRCALPHA)
        p.draw.rect(button_surface, color, (0, 0, self.width, self.height), border_radius=16)
        win.blit(button_surface, self.rect)

        text_surf = FONT_BUTTON.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center) # centre le texte dans le bouton
        shadow = FONT_BUTTON.render(self.text, True, SHADOW)
        win.blit(shadow, (text_rect.x+2, text_rect.y+2))
        win.blit(text_surf, text_rect)
        
    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]


def start_menu():
    """Menu avant lancement du jeu"""
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), p.FULLSCREEN | p.SCALED)
    clock = p.time.Clock()

    ## Ressources
    background = p.image.load("assets/images/menuBg.jpg")
    background=p.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    # List des boutons

    buttons =  [
        Button("Jouer", 320, "play"),
        Button("Quitter", 400, "quit")
    ]


    running = True
    while running:
        clock.tick(60)
        screen.blit(background, (0,0))

        mouse_pos = p.mouse.get_pos()
        mouse_pressed = p.mouse.get_pressed()

        title = FONT_TITLE.render("Mirror Skies", True, WHITE)
        shadow = FONT_TITLE.render("Mirror Skies", True, SHADOW)
        screen.blit(shadow, (SCREEN_WIDTH//2 - title.get_width()//2 + 3, int(title.get_height()) + 3))
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, int(title.get_height())))
        

        for btn in buttons:
            btn.draw(screen, mouse_pos)
            if btn.is_clicked(mouse_pos, mouse_pressed):
                p.time.delay(200)
                if btn.action == "play":
                    return "play"
                elif btn.action == "quit":
                    return "quit"
        
        for event in p.event.get():
            if event.type == p.QUIT:
                return "quit"
        p.display.flip()

def pause_menu(screen):
    """Menu de pause une fois en jeu"""
    #screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), p.FULLSCREEN | p.SCALED)
    clock = p.time.Clock()

    ## Ressources
    background = p.image.load("assets/images/pauseBg.jpg")
    background=p.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    # List des boutons

    buttons =  [
        Button("Continuer", 320, "continue"),
        Button("Quitter", 400, "quit")
    ]

    p.event.clear # Evite les actions parasites

    running = True
    while running:
        clock.tick(60)
        screen.blit(background, (0,0))

        mouse_pos = p.mouse.get_pos()
        mouse_pressed = p.mouse.get_pressed()

        title = FONT_TITLE.render("Pause", True, WHITE)
        shadow = FONT_TITLE.render("Pause", True, SHADOW)
        screen.blit(shadow, (SCREEN_WIDTH//2 - title.get_width()//2 + 3, int(title.get_height()) + 3))
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, int(title.get_height())))
        

        for btn in buttons:
            btn.draw(screen, mouse_pos)
            if btn.is_clicked(mouse_pos, mouse_pressed):
                p.time.delay(200)
                return btn.action
        
        for event in p.event.get():
            if event.type == p.QUIT:
                return "quit"
            if event.type == p.KEYDOWN:
                if event.key == p.K_p:
                    return "continue"
        p.display.flip()