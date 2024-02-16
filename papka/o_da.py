import time
from random import randint
from time import time as timer

import pygame
from pygame import sprite, display, transform, image, font


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class Player(GameSprite):
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def move(self):
        print(player)
        return player[3]

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 40, -15)
        bulletz.add(bullet)


bullet_flag = False


class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y <= win_height:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(80, win_width - 80)
            lost = lost + 1


class Asteroid(GameSprite):
    def update(self):
        global lost
        if self.rect.y <= win_height:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(80, win_width - 80)


win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(image.load("space.png"), (700, 500))
game = True

font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 50)
win = font1.render("You win!", True, (255, 255, 255))
lose = font1.render("You lose!", True, (180, 0, 0))

num_bullets = 5

player = Player('ship2.png', 25, win_height - 100, 80, 100, 10)
monster1 = Enemy('who2.png', randint(0, win_width - 80), 0, 80, 50, randint(2, 7))
monster2 = Enemy('who2.png', randint(0, win_width - 80), 0, 80, 50, randint(2, 7))
monster3 = Enemy('who2.png', randint(0, win_width - 80), 0, 80, 50, randint(2, 7))
monster4 = Enemy('who2.png', randint(0, win_width - 80), 0, 80, 50, randint(2, 7))
monster5 = Enemy('who2.png', randint(0, win_width - 80), 0, 80, 50, randint(2, 7))

asteroid1 = Asteroid('img_1.png', randint(0, win_width - 80), 0, 80, 50, randint(2, 7))
asteroid2 = Asteroid('img_1.png', randint(0, win_width - 80), 0, 80, 50, randint(2, 7))

monsters = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)

asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)

img_bullet = "laser2.png"

bulletz = sprite.Group()

lost = 0
score = 0
goal = 10
max_lost = 10
life = 6

speed = 5
clock = pygame.time.Clock()
FPS = 600

finish = False

pygame.mixer.init()
pygame.mixer.music.load('gimn-rossiyskoy-federatsii-so-slovami-natsionalnyiy-2556.ogg')
pygame.mixer.music.play()
pygame.fire_sound = pygame.mixer.Sound("shoot.ogg")

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if num_bullets >= 0 and bullet_flag is False:
                    pygame.fire_sound.play()
                    player.fire()
                    num_bullets = num_bullets - 1
                if num_bullets <= 0 and bullet_flag is False:
                    bullet_flag = True
                    last_time = timer()

    if not finish:
        text_lose = font1.render("Пропустил:" + str(lost), 1, (255, 255, 255))
        text_babylya = font2.render("Счёт:" + str(score), 1, (255, 255, 255))

        window.blit(background, (0, 0))
        player.reset()
        player.update()
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()

        bulletz.draw(window)
        bulletz.update()
        collides = sprite.groupcollide(monsters, bulletz, True, True)
        collides2 = sprite.spritecollide(player, monsters, False)
        collides3 = sprite.spritecollide(player, asteroids, False)
        text_life = font1.render(str(life), 1, (0, 150, 0))

        if bullet_flag:
            now_time = timer()
            if now_time - last_time < 1:
                reload = font2.render('Lox', 1, (150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_bullets = 5
                bullet_flag = False

        for c in collides:
            monster = Enemy('who2.png', randint(80, win_width - 80), -40, 80, 50, randint(2, 6))
            monsters.add(monster)
            score += 1
            text_babylya = font2.render("Счёт:" + str(score), 1, (255, 255, 255))

        for c in collides2:
            monster = Enemy('who2.png', randint(80, win_width - 80), -40, 80, 50, randint(2, 7))
            monsters.add(monster)

        for c in collides3:
            asteroid = Asteroid('img_1.png', randint(80, win_width - 80), -40, 80, 50, randint(2, 7))
            asteroid.add(asteroids)

        if sprite.spritecollide(player, monsters, False) or sprite.spritecollide(player, asteroids, False):
            sprite.spritecollide(player, monsters, True)
            sprite.spritecollide(player, asteroids, True)
            life = life - 1
            text_life = font1.render(str(life), 1, (0, 150, 0))

        if life == 0 or lost >= max_lost:
            text_lose = font1.render("Пропустил:" + str(lost), 1, (255, 255, 255))
            window.blit(lose, (200, 200))
            finish = True

        if score >= goal:
            window.blit(win, (200, 200))
            finish = True

        window.blit(text_lose, (10, 50))
        window.blit(text_babylya, (10, 20))
        window.blit(text_life, (650, 10))

        display.update()
        clock.tick(FPS)
        pygame.time.delay(20)
