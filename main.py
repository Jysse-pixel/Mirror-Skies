import pygame as p
import random as r
import math
import time

p.init()

clock = p.time.Clock()
FPS = 60

##################### Screen ##################### 
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

MID_SCREEN_HEIGHT = SCREEN_HEIGHT//2
MID_SCREEN_WIDTH = SCREEN_WIDTH//2

screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Prototype VISI")

##################### Récupération images ##################### 
bg = p.image.load("img/bg.png").convert() # Récup img bg
game_over_surface = p.transform.scale2x(p.image.load("game_over.jpg").convert())

##################### Rectangles ############################
playerA = p.Rect((200, 100, 50, 50))
#playerB = p.Rect((200, MID_SCREEN_WIDTH//2, 50, 50))
#playerB = p.Rect(SCREEN_HEIGHT - playerA.y - 50, playerA.y, 50, 50)

platform = p.Rect((800, 200, 200, 50))
game_over_rect = game_over_surface.get_rect(center = (750, 300))

# Charge le background
screen.blit(bg, (0, 0))
bg_width = bg.get_width()
bg_rect = bg.get_rect()

##################### Classes ################################

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
    
    def draw(self, surface):
        ratio = self.hp / self.max_hp
        p.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        p.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))


##################### Définir les variables du jeu #####################
clock = p.time.Clock()
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1 # Le + 1  permet une transition fluide entr eles images
negatif = -1
game_active = True # not game_active = Game over
health_bar = HealthBar(10, 10, 300, 40, 100)
# health_bar.hp = 50

##################### Custom Event ################################

INVINCIBLE_END = p.USEREVENT + 0

##################### Fonctions ################################

def set_invincible_jA():
    invincible_jA = False
    p.time.set_timer(INVINCIBLE_END, 1000, 1)
    return invincible_jA

def check_collision(platform):
    """Vérifie les collision entre une (1) plateforme et le joueur. A généraliser avec une liste de plateformes.
        Entrée : platforme, un rectangle
        Sortie : un boulean, True si collision, False sinon.
    """

    invincible = set_invincible_jA()
    if playerA.colliderect(platform) and not invincible:
        health_bar.hp = health_bar.hp - 10
        #return False
    
    if playerA.top <= 0 or playerA.bottom >= 600 or playerA.left <= 0 or playerA.right >= 1500 or health_bar.hp == 0: # Collisions au bord de l'écran ou vie à 0
        return False

    return True


run = True


#--------------------------------------------------- MAIN MENU --------------------------------------#
def main_menu(): #Main Menu Screen
    while run:
        screen.blit("img/menu_bg", (0,0))

        MENU_MOUSE_POS = p.mouse.get_pos()

        MENU_TEXT = "MAIN MENU"
        MENU_RECT = MENU_TEXT.get_rect(center=(MID_SCREEN_HEIGHT, MID_SCREEN_WIDTH))

        
#--------------------------------------------------- PLAY --------------------------------------#

while run:

    clock.tick(FPS) # Permet de rendre le jeu plus stable (à developper)
    screen.fill("black")
    ##################### Scroll background ##################### 

    # Affiche scrolling bg
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        p.draw.rect(screen, (255,0,0), bg_rect, 1)

    # Scroll bg
    scroll -=5

    # Reset scroll
    if abs(scroll) > bg_width:
        scroll = 0
        
    # Game restart/ Game over
    key = p.key.get_pressed()  # Récupérer la touche pressée
    if key[p.K_r] and not game_active:
        screen.blit(game_over_surface, game_over_rect)
        game_active = True
        health_bar.hp = health_bar.max_hp
        playerA.center = (225, 250)
        platform.center = (800, 200)



    if game_active:

        ##################### Affichage des éléments ########################

        p.draw.rect(screen, (255, 0, 0), playerA)
        health_bar.draw(screen) # Afficher la vie

        p.draw.rect(screen, (0, 255, 0), platform)
        p.draw.line(screen, (0,255,0), (0, MID_SCREEN_HEIGHT), (SCREEN_WIDTH, MID_SCREEN_HEIGHT), 3)
        
        playerB = p.Rect((playerA.x, 550 - playerA.y , 50, 50))
        p.draw.rect(screen, (0, 0, 255), playerB)
        vel_x = -5
        vel_y=0

        ##################### Mouvements joueur 1 ################################

        k = p.key.get_pressed()
        if k[p.K_DOWN]:
            playerA.y += 5
        if k[p.K_UP]:
            playerA.y -= 5
        if k[p.K_RIGHT]:
            playerA.x += 5
        if k[p.K_LEFT]:
            playerA.x -= 5

        playerA.y = max(0, min(playerA.y, MID_SCREEN_HEIGHT - 50))


        ##################### Scroll platform
        platform.centerx += negatif

        ####################### Collisions
        game_active = check_collision(platform)

    ##################### Event Handler ###########################
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

        #if event.type == INVINCIBLE_END:
        #    playerA.invincible = False 

    p.display.flip()

p.QUIT


######### TO DO ##############
# Suprimer un élément qui sort de l'écran
# FAIRE CLASSES JOUEUR
# Position PlayerA après rénitialisation OK
# Centrer PlayerB OK
# Collision PlayerA et B OK