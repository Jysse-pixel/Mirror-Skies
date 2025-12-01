import pygame as p

def start_menu():
    p.display.init()
    info = p.display.Info()
    screen = p.display.set_mode((info.current_w, info.current_h), p.FULLSCREEN)
    clock = p.time.Clock()
    font = p.font.SysFont(None, max(36, info.current_h // 20))
    btn_w, btn_h = info.current_w // 5, info.current_h // 8
    btn_rect = p.Rect((info.current_w - btn_w) // 2, (info.current_h - btn_h) // 2, btn_w, btn_h)
    running = True
    while running:
        for ev in p.event.get():
            if ev.type == p.QUIT:
                p.quit()
                raise SystemExit
            if ev.type == p.KEYDOWN and ev.key == p.K_ESCAPE:
                p.quit()
                raise SystemExit
            if ev.type == p.MOUSEBUTTONDOWN and ev.button == 1:
                if btn_rect.collidepoint(ev.pos):
                    running = False
        screen.fill((0, 0, 0))
        p.draw.rect(screen, (255, 255, 255), btn_rect)
        text = font.render("Jouer", True, (0, 0, 0))
        tx = text.get_rect(center=btn_rect.center)
        screen.blit(text, tx)
        p.display.flip()
        clock.tick(60)