import pygame as p

class SpeedBonus:
    def __init__(self, x, y, size=30, image="assets/images/potion_square_blue.png"):
        self.rect = p.Rect(x, y, size, size)
        self.x_float = float(x)
        self.color = (0, 100, 255)
        self.type = "speed"

        self.image=p.image.load(image).convert_alpha()
        self.image = p.transform.scale(self.image, (50, 50))

    def update(self, scroll_speed):
        self.x_float += scroll_speed
        self.rect.x = int(self.x_float)

    def draw(self, screen):
        #p.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, self)

class HealthBonus:
    def __init__(self, x, y, size=30, image ="assets/images/potion_round_red.png"):
        self.rect = p.Rect(x, y, size, size)
        self.x_float = float(x)
        self.color = (0, 255, 0)
        self.type = "health"

        self.image=p.image.load(image).convert_alpha()
        self.image = p.transform.scale(self.image, (50, 50))

    def update(self, scroll_speed):
        self.x_float += scroll_speed
        self.rect.x = int(self.x_float)

    def draw(self, screen):
        #p.draw.rect(screen, self.color, self.rect)
        
        #center_x, center_y = self.rect.center
        #p.draw.rect(screen, (255, 255, 255), (center_x - 10, center_y - 3, 20, 6))
        #p.draw.rect(screen, (255, 255, 255), (center_x - 3, center_y - 10, 6, 20))
        screen.blit(self.image, self)