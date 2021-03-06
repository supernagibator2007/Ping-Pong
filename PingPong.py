from pygame import *

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

class Player(GameSprite):
    def update_i(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 635:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 635:
            self.rect.y += self.speed


window = display.set_mode((1100, 750))
display.set_caption('PingPong')
background = transform.scale(image.load('background.png'), (1100, 750))

font.init()
font = font.SysFont('Arial', 36)

player1 = Player('pong.png', 0, 325, 200, 200, 15)
player2 = Player('pong.png', 900, 325, 200, 200, 15)
ball = GameSprite('ping.png', 550, 325, 75, 75, 3)

win = 0
win1 = 0
speed_x = 3
speed_y = 3
clock = time.Clock()
FPS = 60
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player1.update_i()
        player1.reset() 
        player2.update_r()
        player2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        score = font.render('Очки первого:' + str(win), True, (255, 0, 0))
        window.blit(score, (15, 15))
        score1 = font.render('Очки второго:' + str(win1), True, (255, 0, 0))
        window.blit(score1, (850, 15))
        if ball.rect.y > 650 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 1050:
            lose = font.render('Проиграл второй', True, (255, 0, 0))
            window.blit(lose, (450, 325))
            finish = True
        if ball.rect.x < 0:
            lose1 = font.render('Проиграл первый', True, (255, 0, 0))
            window.blit(lose1, (450, 325))
            finish = True   
        if sprite.collide_rect(player1, ball):
            speed_x *= -1
            win += 1
        if sprite.collide_rect(player2, ball):
            speed_x *= -1
            win1 += 1
    display.update()
    clock.tick(FPS)
