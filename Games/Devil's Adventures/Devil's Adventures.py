import pygame

pygame.init()
win = pygame.display.set_mode((1000, 683))

pygame.display.set_caption("Devil's Adventures")

walkright = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png')]
walkleft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png')]

playerstand = pygame.image.load('idle.png')
bg = pygame.image.load('bg.png')

clock = pygame.time.Clock()

jumpSound = pygame.mixer.Sound('jump.wav')
bulletSound = pygame.mixer.Sound('bullet.wav')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

x = 5
y = 425
width = 160
height = 160
speed = 10

isjump = False
jumpcount = 10

left = False
right = False
animcount = 0
lastmove = 'right'

class snaryad():
    def __init__(self, x, y,  radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        # win.blit(

def drawwindow():
    global animcount
    win.blit(bg, (0, 0))
    
    if animcount + 1 >= 30:
        animcount = 0

    if left:
        win.blit(walkleft[animcount // 15], (x, y))
        animcount += 1
    elif right:
        win.blit(walkright[animcount // 15], (x, y))
        animcount += 1
    else:
        win.blit(playerstand, (x, y))

    for bullet in bullets:
        bullet.draw(win)
        
    pygame.display.update()

run = True
bullets = []

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.x < 1000 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        bulletSound.play()
        if lastmove == 'right':
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
               bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        left = True
        right = False
        lastmove = 'left'
    elif keys[pygame.K_RIGHT] and x < 1000 - width:
        x += speed
        left = False
        right = True
        lastmove = 'right'
    else:
        right = False
        left = False
        animcount = 0
    if not(isjump):
        if keys[pygame.K_SPACE]:
            jumpSound.play()
            isjump = True
    else:
        if jumpcount >= -10:
            if jumpcount < 0:
                y += (jumpcount ** 2) / 2
            else:
                y -= (jumpcount ** 2) / 2
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10

    drawwindow()
    
pygame.quit()
