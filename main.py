from pygame import * 

class gameSprite(sprite.Sprite):
    def __init__(self, pi, px, py, ps, w, h):
        super().__init__()
        self.image = transform.scale(image.load(pi), (w, h))
        self.speed = ps
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(gameSprite):
    def update_r(self):
        keys = key.get_rect()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_rect()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (0, 0, 0)
wh = 600
ww = 500
win = display.set_mode((ww, wh))
win_fill(back)

gay = True
finish = False
clock = time.Clock()
FPS = 60 

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE", True, (180, 0 0))
lose2 = font.render("PLAYER 2 LOSE", True, (180, 0 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.tupe == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update()
        racket2.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2):
            speed_x *= -1

    if ball.rect.y > wh-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        
