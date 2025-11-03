import pygame as p
from settings import *
from world.background import Background
from world.level import Level
from world.collisions import check_player_and_bounds
from entities.player import Player
from entities.bullet import Bullet
from ui.hud import HealthBar
from core.input import fired

class Game:
    def __init__(self):
        self.clock = p.time.Clock()
        self.screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), p.FULLSCREEN | p.SCALED)
        p.display.set_caption("Prototype VISI")

        self.bg = Background("assets/images/bg.png")
        self.level = Level()
        self.playerA = Player(200, MID_SCREEN_HEIGHT//2 - PLAYER_SIZE//2)
        self.health = HealthBar(10, 10, 300, 40, 100)
        self.bullets = []
        self.game_active = True

    def reset(self):
        self.game_active = True
        self.playerA.rect.x = 200
        self.playerA.rect.y = MID_SCREEN_HEIGHT//2 - PLAYER_SIZE//2
        self.health.hp = self.health.max_hp
        if self.level.platforms:
            self.level.platforms[0].center = (SCREEN_WIDTH//2, MID_SCREEN_HEIGHT - 100)

    def handle_events(self):
        for e in p.event.get():
            if e.type == p.QUIT:
                return False
            if fired(e) and self.game_active:
                a = self.playerA.rect
                self.bullets.append(Bullet(a.right, a.centery - 4))
                b = self.playerA.mirror_rect(SCREEN_HEIGHT)
                self.bullets.append(Bullet(b.right, b.centery - 4))
        return True

    def update(self):
        self.bg.update()
        if self.game_active:
            self.playerA.handle_input()
            self.level.update()
            for b in list(self.bullets):
                b.update()
                if b.offscreen():
                    self.bullets.remove(b)
                else:
                    for plat in list(self.level.platforms):
                        if b.rect.colliderect(plat):
                            self.level.platforms.remove(plat)
                            self.bullets.remove(b)
                            break
            self.game_active = check_player_and_bounds(self.playerA.rect, self.level.platforms, self.health)
        else:
            k = p.key.get_pressed()
            if k[p.K_r]:
                self.reset()

    def draw(self):
        self.bg.draw(self.screen)
        # traits / debug milieu
        p.draw.line(self.screen, GREEN, (0, MID_SCREEN_HEIGHT), (SCREEN_WIDTH, MID_SCREEN_HEIGHT), 3)

        if self.game_active:
            self.playerA.draw(self.screen)
            b_rect = self.playerA.mirror_rect(SCREEN_HEIGHT)
            p.draw.rect(self.screen, BLUE, b_rect)
            self.level.draw(self.screen)
            for b in self.bullets:
                b.draw(self.screen)
            self.health.draw(self.screen)

        p.display.flip()

    def run(self):
        while True:
            if not self.handle_events():
                break
            self.clock.tick(FPS)
            self.update()
            self.draw()