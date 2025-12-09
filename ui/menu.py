import pygame as p
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def start_menu():
    """Menu avant lancement du jeu"""
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), p.FULLSCREEN | p.SCALED)
    clock = p.time.Clock()
    font = p.font.SysFont(None, 60)
    
    btn_rect = p.Rect(0, 0, 300, 100)
    btn_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    running = True
    while running:
        for ev in p.event.get():
            if ev.type == p.QUIT or (ev.type == p.KEYDOWN and ev.key == p.K_ESCAPE):
                p.quit()

            if ev.type == p.MOUSEBUTTONDOWN and ev.button == 1:
                if btn_rect.collidepoint(ev.pos):
                    running = False

        screen.fill((30, 30, 30))
        
        p.draw.rect(screen, (200, 200, 200), btn_rect, border_radius=10)
        
        text = font.render("JOUER", True, (0, 0, 0))
        text_rect = text.get_rect(center=btn_rect.center)
        screen.blit(text, text_rect)
        
        p.display.flip()
        clock.tick(60)