import pygame, random, sys

# Constantes

W, H = 800, 600
MOITIER = W // 2

# Couleurs des éléments
FOND = "white"
LIGNE = "grey"
JOUEUR_G_C = "red"
JOUEUR_D_C = "blue"
OBST_C = "black"

# Taille des éléments

# Taille des joueurs
PW = 40
PH = 28

# Taille des obstacles
OW = 40
OH = 24

#Vitesse joueur/obstacle
PS, OS = 5, 4

#
P_APPA = 0.01

def jeu():
    pygame.init()
    ecran = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    
    joueur_g = pygame.Rect(MOITIER // 2 - PW // 2, H - 100, PW, PH) # x,y, taille_x, taille_y
    obsG = []
    obsD = []

    # Boucle principale
    while True:
        # Fermeture propre
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Entrées clavier
        k = pygame.key.get_pressed()

        # Touche gauche et droite
        if k[pygame.K_RIGHT]:
            joueur_g.x += PS
        if k[pygame.K_LEFT]:
            joueur_g.x -= PS

        joueur_g.x = max(0, min(joueur_g.x, MOITIER - PW)) # Limite pour ne pas depasser

        rp = pygame.Rect(W - joueur_g.x - PW, joueur_g.y, PW, PH)

        # Spawn obstacles
        if random.random() < P_APPA:
            obsG.append(pygame.Rect(random.randint(0, MOITIER - OW), -OH, OW, OH))
        if random.random() < P_APPA:
            obsD.append(pygame.Rect(random.randint(MOITIER, W - OW), -OH, OW, OH))

        # Mouvements des obstacles
        for ob in obsG:
            ob.y += OS
        for ob in obsD:
            ob.y += OS

        



        # Collisions -> reset
        for ob in obsG:
            if joueur_g.colliderect(ob):
                joueur_g = pygame.Rect(MOITIER // 2 - PW // 2, H - 100, PW, PH)
                obsG.clear()
                obsD.clear()
                break

        for ob in obsD:
            if rp.colliderect(ob):
                joueur_g = pygame.Rect(MOITIER // 2 - PW // 2, H - 100, PW, PH)
                obsG.clear()
                obsD.clear()
                break

        # Tout dessiner
        ecran.fill(FOND)
        pygame.draw.line(ecran, LIGNE, (MOITIER, 0), (MOITIER, H), 3)
        pygame.draw.rect(ecran, JOUEUR_G_C, joueur_g)
        pygame.draw.rect(ecran, JOUEUR_D_C, rp)
        for ob in obsG: 
            pygame.draw.rect(ecran, OBST_C, ob)
        for ob in obsD: 
            pygame.draw.rect(ecran, OBST_C, ob)

        pygame.display.flip()
        clock.tick(60)

jeu()
