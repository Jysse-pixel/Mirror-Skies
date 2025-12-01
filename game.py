import pygame as p
from settings import *
from world.background import Background
from world.level import Level
from world.collisions import *
from entities.player import Player
from entities.bullet import *
from entities.coin import Coin
###### MODIF ENEMY
from entities.enemies import *
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
        self.playerB = Player(200, (SCREEN_HEIGHT//2 + 200), (128, 128, 128)) # TO DO : Coordonnée y à mieux définir.
        self.health = HealthBar(10, 10, 300, 40, 100)
        self.bullets = []
        self.game_active = True

        # MODIF - ENEMY
        self.enemies = [
        TestEnemy(MID_SCREEN_WIDTH, 150, 80, 80, 5, 0, 5, False, (255,192,203), mode="mobile"),
        TestEnemy(MID_SCREEN_WIDTH, 200, 300, 80, 80, 3, 0, False, (200,200,50), mode="mobile"),
        TestEnemy(MID_SCREEN_WIDTH + 200, 350, 60, 60, 3, 0, 0, False, (200,150,60), mode="turret")
        ]

        
        self.enemy_bullets = []   # nouvelles balles ennemies

        # Système de scoring
        self.score = 0
        self.coins = []
        self.init_coins()

    def init_coins(self):
        """Initialise les pièces dans le niveau. Note : a move"""
        self.coins = [
            Coin(400, 200),
            Coin(600, 150),
            Coin(800, 250),
            Coin(1000, 180),
            Coin(700, 400),
            Coin(900, 350),
    ]

    def reset(self):
        #self.game_active = True
        self.game_active = check_player_and_bounds(self.playerA.rect, self.level.platforms, self.health)
        self.playerA.rect.x = 200
        self.playerA.rect.y = MID_SCREEN_HEIGHT//2 - PLAYER_SIZE//2

        self.game_active = check_player_and_bounds(self.playerB.rect, self.level.platforms, self.health)
        self.playerB.rect.x = 200
        self.playerB.rect.y = SCREEN_HEIGHT//2 + 200

        self.health.hp = self.health.max_hp
        if self.level.platforms:
            self.level.platforms[0].center = (SCREEN_WIDTH//2, MID_SCREEN_HEIGHT - 100)

        # Reset du score et des pièces
        self.score = 0
        self.init_coins()

    def handle_events(self):
        for e in p.event.get():
            if e.type == p.QUIT:
                return False
            if fired(e) and self.game_active:
                jr_a = self.playerA.rect
                self.bullets.append(Bullet(jr_a.right, jr_a.centery - 4))
                jr_b = self.playerB.rect
                self.bullets.append(Bullet(jr_b.right, jr_b.centery -4))
        return True

    def update(self):
        self.bg.update()
        if self.game_active:
            self.playerA.handle_input()
            self.playerB.handle_input_mirror()
            self.level.update()
            
            for coin in self.coins:
                coin.update()

            self.score += check_coin_collection(self.coins, self.playerA.rect)
            self.score += check_coin_collection(self.coins, self.playerB.rect)

            for enemy in self.enemies:
                enemy.move()
                enemy.update_color()

                if enemy.mode == "turret":
                    fire = enemy.try_fire(self.playerA.rect)
                    if fire:
                        x, y, vx, vy = fire
                        self.enemy_bullets.append(EnemyBullet(x, y, vx, vy))

            # Gestion des balles ennemies ###
            for eb in list(self.enemy_bullets):
                eb.update()

                # si la balle touche un joueur
                if eb.rect.colliderect(self.playerA.rect) or eb.rect.colliderect(self.playerB.rect):
                    self.health.hp -= 1
                    self.enemy_bullets.remove(eb)
                    continue

                # hors écran
                if eb.offscreen():
                    self.enemy_bullets.remove(eb)
            #####

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

                    for enemy in list(self.enemies):
                        if b.rect.colliderect(enemy.rect):
                            dead = enemy.hit()
                            self.bullets.remove(b)
                            self.color = (255,0,0)

                            # Ennemi détruit
                            if dead:
                                self.enemies.remove(enemy)

                            break  # on arrête de tester d’autres ennemis pour cette balle

            aliveA = check_player_and_bounds(self.playerA.rect, self.level.platforms, self.health)
            aliveB = check_player_and_bounds(self.playerB.rect, self.level.platforms, self.health)

            touchA = all(check_player_and_enemy(self.playerA.rect, enemy, self.health) for enemy in self.enemies)
            touchB = all(check_player_and_enemy(self.playerB.rect, enemy, self.health) for enemy in self.enemies)

            self.game_active = aliveA and aliveB and touchA and touchB

        
        else:
            k = p.key.get_pressed()
            if k[p.K_r]:
                self.reset()
        k = p.key.get_pressed()
        if k[p.K_e]:
                p.quit()

    def draw(self):
        self.bg.draw(self.screen)
        # traits / debug milieu
        p.draw.line(self.screen, GREEN, (0, MID_SCREEN_HEIGHT), (SCREEN_WIDTH, MID_SCREEN_HEIGHT), 3)

        if self.game_active:
            self.playerA.draw(self.screen)
            self.playerB.draw(self.screen)
            self.level.draw(self.screen)

            Coin.draw_all(self.screen, self.coins)

            for b in self.bullets:
                b.draw(self.screen)
            self.health.draw(self.screen)
            
            #### MODIF - AFICHER L'ENEMY
            for enemy in self.enemies:
                enemy.draw(self.screen)

            for eb in self.enemy_bullets:
                eb.draw(self.screen)

            self.draw_score()

        p.display.flip()

    def draw_score(self):
        """Affiche le score à l'écran. Note : je laissa ça là temporairement."""
        font = p.font.Font(None, 48)
        score_text = font.render(f"Score: {self.score}", True, (255, 215, 0))
        score_shadow = font.render(f"Score: {self.score}", True, (0, 0, 0))
        
        # Ombre
        self.screen.blit(score_shadow, (SCREEN_WIDTH - 252, 12))
        # Texte
        self.screen.blit(score_text, (SCREEN_WIDTH - 250, 10))

    def run(self):
        while True:
            if not self.handle_events():
                break
            self.clock.tick(FPS)
            self.update()
            self.draw()