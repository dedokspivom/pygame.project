from random import randint
from time import time as timer

import pygame
from pygame import sprite, display, transform, image, font

difficulty = {
    "speed": 1,
    "frequency": 1,
}


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed * difficulty["speed"]
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
        global text_lose
        if self.rect.y <= win_height:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(80, win_width - 80)
            lost = lost + 1
            text_lose = font1.render("Пропустил:" + str(lost), 1, (255, 255, 255))


class Asteroid(GameSprite):
    def update(self):
        global lost
        if self.rect.y <= win_height:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(80, win_width - 80)


def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.Font('combine-17_0.ttf', 75)
    font1 = pygame.font.SysFont('arial', 17)

    title = font.render('GALAXY WARS THE GREATEST BRAWL', True, (255, 255, 255))
    start_button = font1.render('Press "space" button to start', True, (255, 255, 255))
    settings_button = font1.render('Press "s" button for settings', True, (255, 255, 255))
    citata_button = font1.render('Press "c" button for citata', True, (255, 255, 255))
    screen.blit(title, (win_width / 2 - title.get_width() / 2, win_height / 2 - title.get_height() / 2))
    screen.blit(start_button,
                (win_width / 2 - start_button.get_width() / 2, win_height / 2 + start_button.get_height() / 1.7))
    screen.blit(settings_button,
                (win_width / 2 - start_button.get_width() / 2, win_height / 2 + start_button.get_height() * 1.5))
    screen.blit(citata_button,
                (win_width / 2 - start_button.get_width() / 2, win_height / 2 + start_button.get_height() * 2.5))
    pygame.display.update()


def jeis():
    global background
    background = transform.scale(image.load(f"jei{randint(1, 5)}.jpg"), (700, 500))
    window.blit(background, (0, 0))
    pygame.display.update()
    display.update()


def victory():
    global background
    background = transform.scale(image.load("jei_win.jpg"), (700, 500))
    window.blit(background, (0, 0))
    pygame.display.update()
    display.update()


def defeated():
    global background
    background = transform.scale(image.load("jei_lose.jpg"), (700, 500))
    window.blit(background, (0, 0))
    pygame.display.update()
    display.update()


def draw_settings():
    screen.fill((0, 0, 0))
    font1 = pygame.font.SysFont('arial', 24)
    font2 = pygame.font.SysFont('arial', 36)
    back_button = font2.render("(backspace)Back to start screen", True, (255, 0, 0))
    speed_button = font1.render(f"(k)Choose enemies` speed: {s}", True, (255, 255, 255))
    frequency_button = font1.render(f"(f)Choose enemies` frequency: {freq}", True, (255, 255, 255))
    goal_button = font1.render(f"(g)Choose goal: {goal}", True, (255, 255, 255))
    live_button = font1.render(f"(h)Choose lives: {max_lives}", True, (255, 255, 255))
    lost_button = font1.render(f"(l)Choose misses: {max_lost}", True, (255, 255, 255))
    screen.blit(speed_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - speed_button.get_height() / 2))
    screen.blit(frequency_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 + frequency_button.get_height() / 2))
    screen.blit(goal_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - 3 * speed_button.get_height() / 2))
    screen.blit(live_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - 5 * speed_button.get_height() / 2))
    screen.blit(lost_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - 7 * speed_button.get_height() / 2))
    screen.blit(back_button,
                (win_width / 2 - speed_button.get_width() / 1.5, win_height / 2 - 15 * speed_button.get_height() / 2))
    pygame.display.update()


def speeds():
    global text
    global s
    screen.fill((0, 0, 0))
    font1 = pygame.font.SysFont('arial', 24)
    font2 = pygame.font.SysFont('arial', 36)
    s = ''.join([i for i in text if i.isdigit()])
    gg = font2.render(f'{s}', 1, (150, 150, 0))
    speed_button = font1.render(f"Choose enemies` speed: type int.", True, (255, 255, 255))
    screen.blit(speed_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 4 - speed_button.get_height()))
    screen.blit(gg,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - speed_button.get_height()))
    pygame.display.update()


def freee():
    global txt
    global freq
    screen.fill((0, 0, 0))
    font1 = pygame.font.SysFont('arial', 24)
    font2 = pygame.font.SysFont('arial', 36)
    freq = ''.join([i for i in txt if i.isdigit()])
    gg = font2.render(f'{freq}', 1, (150, 0, 0))
    speed_button = font1.render(f"Choose enemies` frequency: type int.", True, (255, 255, 255))
    screen.blit(speed_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 4 - speed_button.get_height()))
    screen.blit(gg,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - speed_button.get_height()))
    pygame.display.update()


def scorere():
    global goal
    global te
    screen.fill((0, 0, 0))
    font1 = pygame.font.SysFont('arial', 24)
    font2 = pygame.font.SysFont('arial', 36)
    goal = ''.join([i for i in te if i.isdigit()])
    gg = font2.render(f'{goal}', 1, (0, 150, 0))
    speed_button = font1.render(f"Choose goal: type int.", True, (255, 255, 255))
    screen.blit(speed_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 4 - speed_button.get_height()))
    screen.blit(gg,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - speed_button.get_height()))
    pygame.display.update()


def losese():
    global max_lost
    global t
    screen.fill((0, 0, 0))
    font1 = pygame.font.SysFont('arial', 24)
    font2 = pygame.font.SysFont('arial', 36)
    max_lost = ''.join([i for i in t if i.isdigit()])
    gg = font2.render(f'{max_lost}', 1, (0, 0, 255))
    speed_button = font1.render(f"Choose max. misses: type int.", True, (255, 255, 255))
    screen.blit(speed_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 4 - speed_button.get_height()))
    screen.blit(gg,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - speed_button.get_height()))
    pygame.display.update()


def livesese():
    global max_lives
    global tx
    screen.fill((0, 0, 0))
    font1 = pygame.font.SysFont('arial', 24)
    font2 = pygame.font.SysFont('arial', 36)
    max_lives = ''.join([i for i in tx if i.isdigit()])
    gg = font2.render(f'{max_lives}', 1, (255, 0, 255))
    speed_button = font1.render(f"Choose lives: type int.", True, (255, 255, 255))
    screen.blit(speed_button,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 4 - speed_button.get_height()))
    screen.blit(gg,
                (win_width / 2 - speed_button.get_width() / 2, win_height / 2 - speed_button.get_height()))
    pygame.display.update()


win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
screen = display.set_mode((win_width, win_height))
display.set_caption("GALAXY WARS")
background = transform.scale(image.load("space.png"), (700, 500))
game = False

font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 24)
font3 = font.Font(None, 70)
win = font1.render("You win!", True, (255, 255, 255))
lose = font1.render("You lose!", True, (180, 0, 0))
s = 5
freq = 5
goal = 10
max_lost = 10
max_lives = 10
max_goal = 10
speed = 6
clock = pygame.time.Clock()
FPS = 600

img_bullet = "laser2.png"

text = ''
txt = ''
tx = ''
te = ''
t = ''

finish = False
start_game = True
game_state = "start_screen"

pygame.mixer.init()
# pygame.mixer.music.load('gimn-rossiyskoy-federatsii-so-slovami-natsionalnyiy-2556.ogg')
# pygame.mixer.music.play()
pygame.fire_sound = pygame.mixer.Sound("shoot.ogg")
monsters = sprite.Group()
asteroids = sprite.Group()
bulletz = sprite.Group()

player = Player('ship2.png', 25, win_height - 100, 80, 100, 10)

while start_game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            start_game = False
        if game_state == "jeisssss":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_c:
                    jeis()
                if e.key == pygame.K_BACKSPACE:
                    background = transform.scale(image.load("space.png"), (700, 500))
                    game_state = "start_screen"
        if game_state == "start_screen":
            draw_start_menu()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    bulletz = sprite.Group()
                    monsters = sprite.Group()
                    asteroids = sprite.Group()
                    bullet_flag = False
                    num_bullets = 5
                    lost = 0
                    score = 0
                    max_lost = 10
                    life = int(max_lives)
                    text_life = font1.render(f'HP {str(life)}', 1, (0, 150, 0))
                    text_babylya = font1.render("Счёт:" + str(score), 1, (255, 255, 255))
                    text_lose = font1.render("Пропустил:" + str(lost), 1, (255, 255, 255))
                    player.reset()
                    player = Player('ship2.png', 25, win_height - 100, 80, 100, 10)
                    for i in range(int(freq)):
                        monster = Enemy('who2.png', randint(0, win_width - 80), 0, 80, 50,
                                        (speed + int(s) + 5) / 2 - randint(2, 5))
                        monsters.add(monster)
                    for i in range(int(freq) // 2):
                        asteroid = Asteroid('img_1.png', randint(0, win_width - 80), 0, 80, 50,
                                            (speed + int(s) + 5) / 2 - randint(1, 5))
                        asteroids.add(asteroid)
                    start_game = False
                    game = True
                    game_state = "start"
                    finish = False
                if e.key == pygame.K_c:
                    game_state = "jeisssss"
                    jeis()
                if e.key == pygame.K_s:
                    draw_settings()
                    game_state = "settings"
        if game_state == "settings":
            draw_settings()
            if e.type == pygame.QUIT:
                start_game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    game_state = "start_screen"
                if e.key == pygame.K_k:
                    game_state = "speed_screen"
                if e.key == pygame.K_f:
                    game_state = "freq_screen"
                if e.key == pygame.K_g:
                    game_state = "score_screen"
                if e.key == pygame.K_l:
                    game_state = "lose_screen"
                if e.key == pygame.K_h:
                    game_state = "live_screen"
        if game_state == "live_screen":
            if e.type == pygame.QUIT:
                start_game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    game_state = "settings"
                if e.key == pygame.K_BACKSPACE:
                    tx = tx[:-1]
                    livesese()
            if e.type == pygame.TEXTINPUT:
                tx += e.text
                livesese()
        if game_state == "lose_screen":
            if e.type == pygame.QUIT:
                start_game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    game_state = "settings"
                if e.key == pygame.K_BACKSPACE:
                    t = t[:-1]
                    losese()
            if e.type == pygame.TEXTINPUT:
                t += e.text
                losese()
        if game_state == "score_screen":
            if e.type == pygame.QUIT:
                start_game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    game_state = "settings"
                if e.key == pygame.K_BACKSPACE:
                    te = te[:-1]
                    scorere()
            if e.type == pygame.TEXTINPUT:
                te += e.text
                scorere()
        if game_state == "speed_screen":
            if e.type == pygame.QUIT:
                start_game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    game_state = "settings"
                if e.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    speeds()
            if e.type == pygame.TEXTINPUT:
                text += e.text
                speeds()
        if game_state == "freq_screen":
            if e.type == pygame.QUIT:
                start_game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    game_state = "settings"
                if e.key == pygame.K_BACKSPACE:
                    txt = txt[:-1]
                    freee()
            if e.type == pygame.TEXTINPUT:
                txt += e.text
                freee()
        if game_state == 'win':
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_c:
                    victory()
                if e.key == pygame.K_BACKSPACE:
                    background = transform.scale(image.load("space.png"), (700, 500))
                    game_state = "start_screen"
        if game_state == 'lose':
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_c:
                    defeated()
                if e.key == pygame.K_BACKSPACE:
                    background = transform.scale(image.load("space.png"), (700, 500))
                    game_state = "start_screen"
        if game_state == "start":
            while game:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        game = False
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_r:
                            start_game = True
                            game_state = "start_screen"
                            game = False
                            finish = True
                        if e.key == pygame.K_SPACE:
                            if num_bullets >= 0 and bullet_flag is False:
                                pygame.fire_sound.play()
                                player.fire()
                                num_bullets = num_bullets - 1
                            if num_bullets <= 0 and bullet_flag is False:
                                bullet_flag = True
                                last_time = timer()

                if not finish:
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

                    if bullet_flag:
                        now_time = timer()
                        if now_time - last_time < 1:
                            reload = font3.render('Перезарядка', 1, (150, 0, 0))
                            window.blit(reload, (200, 440))
                        else:
                            num_bullets = 5
                            bullet_flag = False

                    for c in collides:
                        monster = Enemy('who2.png', randint(80, win_width - 80), -40, 80, 50,
                                        (speed + int(s) + 5) / 2 - randint(2, 5))
                        monsters.add(monster)
                        score += 1
                        text_babylya = font1.render("Счёт:" + str(score), 1, (255, 255, 255))

                    for c in collides2:
                        monster = Enemy('who2.png', randint(80, win_width - 80), -40, 80, 50,
                                        (speed + int(s) + 5) / 2 - randint(2, 5))
                        monsters.add(monster)

                    for c in collides3:
                        asteroid = Asteroid('img_1.png', randint(80, win_width - 80), -40, 80, 50,
                                            (speed + int(s) + 5) / 2 - randint(2, 5))
                        asteroid.add(asteroids)

                    if sprite.spritecollide(player, monsters, False) or sprite.spritecollide(player, asteroids, False):
                        sprite.spritecollide(player, monsters, True)
                        sprite.spritecollide(player, asteroids, True)
                        life -= 1
                        text_life = font1.render(f'HP {str(life)}', 1, (0, 150, 0))

                    window.blit(text_lose, (10, 50))
                    window.blit(text_babylya, (10, 20))
                    window.blit(text_life, (600 - (len(str(life)) - 1) * 15, 10))


                    if life == 0 or lost >= max_lost:
                        text_lose = font1.render("Пропустил:" + str(lost), 1, (255, 255, 255))
                        window.blit(lose, (200, 200))
                        defeated()
                        start_game = True
                        game_state = 'lose'
                        game = False
                        finish = True

                    if score >= int(goal):
                        window.blit(win, (200, 200))
                        victory()
                        start_game = True
                        game_state = 'win'
                        game = False
                        finish = True

                    display.update()
                    clock.tick(FPS)
                    pygame.time.delay(20)
