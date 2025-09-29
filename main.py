import pygame as p
import math


p.init()

clock = p.time.Clock()
FPS = 60

##################### Screen ##################### 
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Prototype VISI")

##################### Récupération images ##################### 
bg = p.image.load("bg.png").convert() # Récup img bg
game_over_surface = p.transform.scale2x(p.image.load("game_over.jpg").convert())

##################### Rectangles ############################
player = p.Rect((300, 250, 50, 50))
platform = p.Rect((800, 200, 200, 50))
game_over_rect = game_over_surface.get_rect(center = (750, 300))

# Charge le background
screen.blit(bg, (0, 0))
bg_width = bg.get_width()
bg_rect = bg.get_rect()

##################### Définir les variables du jeu #####################
 
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1 # Le + 1  permet une transition fluide entr eles images
negatif = -1
game_active = True # not game_active = Game over


##################### Fonctions ################################

def check_collision(platform):
    """Vérifie les collision entre une (1) plateforme et le joueur. A généraliser avec une liste de plateformes.
        Entrée : platforme, un rectangle
        Sortie : un boulean, True si collision, False sinon.
    """
    if player.colliderect(platform) :
        return False
    
    if player.top <= 0 or player.bottom >= 600 or player.left <= 0 or player.right >= 1500: # Collisions au bord de l'écran
        return False
    
    return True



run = True

#-----------------------------------------------------------------------------------------#

while run:

    clock.tick(FPS) # Permet de rendre le jeu plus stable (à developper)

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
        player.center = (300, 250)
        platform.center = (800, 200)



    if game_active:

        ##################### Affichage des éléments ########################

        p.draw.rect(screen, (255, 0, 0), player)
        p.draw.rect(screen, (0, 255, 0), platform)

        vel_x = -5
        vel_y=0

        ##################### Mouvements joueur 1 ################################

        if key[p.K_q] == True: # Gestion mvt en fonction touche
            player.move_ip(-5, 0)
        elif key[p.K_d] == True:
            player.move_ip(5,0)
        elif key[p.K_z] == True:
            player.move_ip(0, -5)
        elif key[p.K_s] == True:
            player.move_ip(0, 5)


        ##################### Scroll platform
        platform.centerx += negatif

        ####################### Collisions
        game_active = check_collision(platform)

    ##################### Event Handler ###########################
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()

p.QUIT


######### TO DO ##############
# Suprimer un élément qui sort de l'écran