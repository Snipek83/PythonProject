import pygame
import random


#описание констант

WIDTH = 600
HEIGHT = 800
INDENT = 10

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#описание классов

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - INDENT
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH-INDENT:
            self.rect.right = WIDTH-INDENT
        if self.rect.left < INDENT:
            self.rect.left = INDENT

    def shoot(self):
        bullet = Bullet()
        bullets.add(bullet)
        all_sprites.add (bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -30)
        self.speedx = random.randrange(-3, 4)
        self.speedy = random.randrange(1, 8)


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -30)
            self.speedx = random.randrange(-3, 4)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.bottom = player.rect.y
        self.speedy = - 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.midtop = (x, y)
    screen.blit(surface, rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Snipe Game")
clock = pygame.time.Clock()

score = 0
delay = 0
font_name = pygame.font.match_font('arial')

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(10):
    enemy = Enemy()
    enemies.add(enemy)
all_sprites.add(enemies)



#начало программы
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():  # кнопка крестик
        if event.type == pygame.QUIT:  # кнопка крестик
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
            player.shoot()
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        delay = 3000
        running = False

    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 1
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    screen.fill(BLACK)
    draw_text(f' Очки: {score}', 18,WHITE, WIDTH / 2, 10)
    if delay == 0:
        all_sprites.draw(screen)
    else:
        draw_text("Game Over", 50, RED, WIDTH / 2, HEIGHT / 2 - 50)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.time.delay(delay)
pygame.quit()
