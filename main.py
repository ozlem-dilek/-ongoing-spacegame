import pygame
import random

pygame.init()

width = 500
height = 500
window = pygame.display.set_mode((width, height))

FPS = 60
clock = pygame.time.Clock()
score = 0


class Gamer(pygame.sprite.Sprite):
    def __init__(self, gamer_bomb_group):
        super().__init__()
        self.image = pygame.image.load("assets/ufo64.png")
        self.rect = self.image.get_rect()
        self.gamer_bomb_group = gamer_bomb_group
        self.rect.centerx = width / 2
        self.rect.top = height - 70
        self.speed = 25
        self.health = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.right<= width:
            self.rect.x += self.speed

    def fire(self):
        if len(self.gamer_bomb_group)<=2:
            gamerBomb(self.rect.centerx, self.rect.top, self.gamer_bomb_group)



class gamerBomb(pygame.sprite.Sprite):
    def __init__(self, x, y, gamer_bomb_group):
         super().__init__()
         self.image = pygame.image.load("assets/bomb.png")
         self.rect = self.image.get_rect()
         self.rect.centerx = x
         self.rect.centery = y
         self.speed = 25
         gamer_bomb_group.add(self)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class asteroid(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.image = pygame.image.load("assets/asteroid.png")
         self.rect = self.image.get_rect()
         self.rect.x = random.randint(0, width-32)
         self.rect.y = random.randint(0, height-80)
         asteroid_group.add(self)



gamer_bomb_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
ast = asteroid()
asteroid_group.add(ast)
gamer_group = pygame.sprite.Group()
gamer = Gamer(gamer_bomb_group)
gamer_group.add(gamer)





status = True
while status:
    for act in pygame.event.get():
        if act.type == pygame.QUIT:
            status = False

        if act.type == pygame.KEYDOWN:
            if act.key == pygame.K_SPACE:
                gamer.fire()


    for bomb in gamer_bomb_group:
        if ast.rect.colliderect(bomb):
            ast.rect.x = random.randint(0, width-32)
            ast.rect.y = random.randint(0, height-132)
            score +=1

    window.fill((0, 0, 0))
    gamer_group.update()
    gamer_group.draw(window)
    gamer_bomb_group.update()
    gamer_bomb_group.draw(window)
    asteroid_group.update()
    asteroid_group.draw(window)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
