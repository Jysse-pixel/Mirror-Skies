import pygame as p
from settings import *
from world.background import Background
from world.level import Level
from world.collisions import check_collisions_and_bounds
from entities.player import Player
from entities.bullet import Bullet, EnemyBullet
from ui.hud import HealthBar
from core.input import fired
from ui.menu import start_menu, pause_menu

class Game:
    def __init__(self):
        self.screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), p.FULLSCREEN | p.SCALED)
        p.display.set_caption("Mirror Skies")
        self.clock = p.time.Clock()
        self.font = p.font.SysFont(None, 48)

        self.bg = Background("assets/images/bg.png")
        self.level = Level()
        
       
        self.playerA = Player(200, MID_SCREEN_HEIGHT // 2)

        self.playerB_image = p.image.load("assets/images/joueur2.png").convert_alpha()
        self.playerB_image = p.transform.scale(self.playerB_image, (80, 60))
        
        self.health = HealthBar(10, 10, 300, 30, 100)
        self.bullets = []
        self.enemy_bullets = []
        
        self.score = 0
        self.game_active = True
        self.victory = False

    def reset(self):
        self.game_active = True
        self.victory = False
        self.playerA = Player(200, MID_SCREEN_HEIGHT // 2)
        self.bullets.clear()
        self.enemy_bullets.clear()
        self.score = 0
        self.health.hp = self.health.max_hp
        self.level = Level() 

    def handle_events(self):
        for e in p.event.get():
            if e.type == p.QUIT:
                return False
            
            # Gestion du tir 
            if fired(e) and self.game_active:
                # Tir Joueur A
                self.bullets.append(Bullet(self.playerA.rect.right, self.playerA.rect.centery))
                # Tir Joueur B
                rect_b = self.playerA.get_mirror_rect(SCREEN_HEIGHT)
                self.bullets.append(Bullet(rect_b.right, rect_b.centery))

            if e.type == p.KEYDOWN:
                if e.key == p.K_r and not self.game_active:
                    self.reset()
                
                # Menu Pause
                if e.key == p.K_ESCAPE or e.key == p.K_p:
                    action = pause_menu(self.screen)
                    if action == "quit":
                        return False

        return True

    def update(self):
        self.bg.update()
        
        if self.game_active:
       
            self.playerA.update()
            
            rect_b = self.playerA.get_mirror_rect(SCREEN_HEIGHT)
            
            self.level.update()

            if self.level.is_finished():
                self.game_active = False
                self.victory = True

            for plat in list(self.level.platforms):
                if self.playerA.rect.colliderect(plat) or rect_b.colliderect(plat):
                    self.health.hp -= 1

            for b in list(self.bullets):
                b.update()
                bullet_active = True 

                if b.offscreen():
                    self.bullets.remove(b)
                    bullet_active = False
                
                if bullet_active:
                    for plat in list(self.level.platforms):
                        if bullet_active and b.rect.colliderect(plat):
                            self.bullets.remove(b)
                            bullet_active = False
                            if plat.destructible:
                                if plat.take_damage():
                                    self.level.platforms.remove(plat)
                                    self.score += 5
                
                if bullet_active:
                    for enemy in list(self.level.enemies):
                        if bullet_active and b.rect.colliderect(enemy.rect):
                            self.bullets.remove(b)
                            bullet_active = False
                            if enemy.hit():
                                self.level.enemies.remove(enemy)
                                self.score += 10

            for enemy in self.level.enemies:
                # Calculer la distance vers chaque joueur
                rect_b = self.playerA.get_mirror_rect(SCREEN_HEIGHT)
                
                dist_to_A = ((enemy.rect.centerx - self.playerA.rect.centerx)**2 + 
                            (enemy.rect.centery - self.playerA.rect.centery)**2)**0.5
                dist_to_B = ((enemy.rect.centerx - rect_b.centerx)**2 + 
                            (enemy.rect.centery - rect_b.centery)**2)**0.5
                
                # Viser le joueur le plus proche
                target = self.playerA.rect if dist_to_A <= dist_to_B else rect_b

                fire_data = enemy.try_fire(target)
                if fire_data:
                    x, y, vx, vy = fire_data
                    self.enemy_bullets.append(EnemyBullet(x, y, vx, vy))

            for eb in list(self.enemy_bullets):
                eb.update()
                if eb.offscreen():
                    self.enemy_bullets.remove(eb)
                elif eb.rect.colliderect(self.playerA.rect) or eb.rect.colliderect(rect_b):
                    self.health.hp -= 10
                    self.enemy_bullets.remove(eb)


            for coin in list(self.level.coins):
                if self.playerA.rect.colliderect(coin.rect) or rect_b.colliderect(coin.rect):
                    self.level.coins.remove(coin)
                    self.score += 1

            for bonus in list(self.level.bonuses):
                if self.playerA.rect.colliderect(bonus.rect):
                    if bonus.type == "speed":
                        self.playerA.activate_speed_bonus()
                        self.level.bonuses.remove(bonus)
                    elif bonus.type == "health":
                        heal_amount = self.health.max_hp * 0.5
                        self.health.hp = min(self.health.max_hp, self.health.hp + heal_amount)
                        self.level.bonuses.remove(bonus)

            for enemy in self.level.enemies:
                if self.playerA.rect.colliderect(enemy.rect) or rect_b.colliderect(enemy.rect):
                    self.health.hp -= 1

            alive_a = check_collisions_and_bounds(self.playerA.rect, self.level.platforms, SCREEN_WIDTH, MID_SCREEN_HEIGHT)
            alive_b = check_collisions_and_bounds(rect_b, self.level.platforms, SCREEN_WIDTH, SCREEN_HEIGHT)
            
            if rect_b.top < MID_SCREEN_HEIGHT:
                alive_b = False

            if not alive_a or not alive_b or self.health.hp <= 0:
                self.game_active = False

    def draw_text_with_outline(self, text, x, y, color):
        base = self.font.render(text, True, color)
        outline = self.font.render(text, True, BLACK)
        
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            self.screen.blit(outline, outline.get_rect(center=(x + dx, y + dy)))

        self.screen.blit(base, base.get_rect(center=(x, y)))

    def draw(self):
        self.bg.draw(self.screen)
        
        p.draw.line(self.screen, GREEN, (0, MID_SCREEN_HEIGHT), (SCREEN_WIDTH, MID_SCREEN_HEIGHT), 3)

        if self.game_active:
            self.playerA.draw(self.screen)
            rect_b = self.playerA.get_mirror_rect(SCREEN_HEIGHT)
            self.screen.blit(self.playerB_image, rect_b)
            
            self.level.draw(self.screen)
            
            for b in self.bullets:
                b.draw(self.screen)
            for eb in self.enemy_bullets:
                eb.draw(self.screen)
                
            self.health.draw(self.screen)
            
            score_surf = self.font.render(f"Score : {self.score}", True, YELLOW)
            self.screen.blit(score_surf, (SCREEN_WIDTH - 200, 10))
        else:
            if self.victory:
                self.draw_text_with_outline("NIVEAU TERMINE - Score : " + str(self.score), MID_SCREEN_WIDTH, MID_SCREEN_HEIGHT - 200, GREEN)
            else:
                over_text = self.font.render("GAME OVER - Appuyez sur R pour réessayer !", True, RED)
                center_rect = over_text.get_rect(center=(MID_SCREEN_WIDTH, MID_SCREEN_HEIGHT))
                self.screen.blit(over_text, center_rect)

        p.display.flip()

    def run(self):
        # Variable de contrôle globale (running)
        running = True
        while running:
            running = self.handle_events()
        
            if running:
                self.clock.tick(FPS)
                self.update()
                self.draw()