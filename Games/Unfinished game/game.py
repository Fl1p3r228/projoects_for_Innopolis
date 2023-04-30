import pygame

pygame.init()

walk_down = [pygame.image.load('S-S1.png'), pygame.image.load('S-S2.png'), pygame.image.load('S-S3.png'),
             pygame.image.load('S-S4.png'), pygame.image.load('S-S5.png'), pygame.image.load('S-S6.png'),
             pygame.image.load('S-S7.png'), pygame.image.load('S-S8.png')]
walk_up = [pygame.image.load('S-W1.png'), pygame.image.load('S-W2.png'), pygame.image.load('S-W3.png'),
           pygame.image.load('S-W4.png'), pygame.image.load('S-W5.png'), pygame.image.load('S-W6.png'),
           pygame.image.load('S-W7.png'), pygame.image.load('S-W8.png')]
walk_right = [pygame.image.load('S-D1.png'), pygame.image.load('S-D2.png'), pygame.image.load('S-D3.png'),
              pygame.image.load('S-D4.png'), pygame.image.load('S-D5.png'), pygame.image.load('S-D6.png'),
              pygame.image.load('S-D7.png'), pygame.image.load('S-D8.png')]
walk_left = [pygame.image.load('S-A1.png'), pygame.image.load('S-A2.png'), pygame.image.load('S-A3.png'),
             pygame.image.load('S-A4.png'), pygame.image.load('S-A5.png'), pygame.image.load('S-A6.png'),
             pygame.image.load('S-A7.png'), pygame.image.load('S-A8.png')]


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self):
        global camera_x, camera_y, x, y, character_x, character_y
        if 100 < character_x < 768 - 200:
            camera_x += self.dx
            x += self.dx
        if 100 < character_y < height - 200:
            camera_y += self.dy
            y += self.dy

    def update(self):
        global x, y
        self.dx = -(x + 18 - width // 2)
        self.dy = -(y + 28 - height // 2)


camera_x = -254
camera_y = -284
width = 1024
height = 720
dis = pygame.display.set_mode((width, height))
walk_down = [pygame.image.load('S-S1.png'), pygame.image.load('S-S2.png'), pygame.image.load('S-S3.png'),
             pygame.image.load('S-S4.png'), pygame.image.load('S-S5.png'), pygame.image.load('S-S6.png'),
             pygame.image.load('S-S7.png'), pygame.image.load('S-S8.png')]
walk_up = [pygame.image.load('S-W1.png'), pygame.image.load('S-W2.png'), pygame.image.load('S-W3.png'),
           pygame.image.load('S-W4.png'), pygame.image.load('S-W5.png'), pygame.image.load('S-W6.png'),
           pygame.image.load('S-W7.png'), pygame.image.load('S-W8.png')]
walk_right = [pygame.image.load('S-D1.png'), pygame.image.load('S-D2.png'), pygame.image.load('S-D3.png'),
              pygame.image.load('S-D4.png'), pygame.image.load('S-D5.png'), pygame.image.load('S-D6.png'),
              pygame.image.load('S-D7.png'), pygame.image.load('S-D8.png')]
walk_left = [pygame.image.load('S-A1.png'), pygame.image.load('S-A2.png'), pygame.image.load('S-A3.png'),
             pygame.image.load('S-A4.png'), pygame.image.load('S-A5.png'), pygame.image.load('S-A6.png'),
             pygame.image.load('S-A7.png'), pygame.image.load('S-A8.png')]
game_over = False
speed = 2
x = 192
y = 256
character_x = 135 + x
character_y = 50 + y
camera = Camera()
clock = pygame.time.Clock()
goes_down = True
goes_up = False
goes_left = False
goes_right = False
anime = 0


def drawWindow():
    global anime
    dis.blit(pygame.image.load('lop.jpeg'), (camera_x, camera_y))
    if anime + 1 >= 64:
        anime = 0
    if goes_down:
        dis.blit(walk_down[anime // 8], (x, y))
        anime += 1
    if goes_up:
        dis.blit(walk_up[anime // 8], (x, y))
        anime += 1
    if goes_right:
        dis.blit(walk_right[anime // 8], (x, y))
        anime += 1
    if goes_left:
        dis.blit(walk_left[anime // 8], (x, y))
        anime += 1
        
    pygame.display.update()


while not game_over:
    clock.tick(64)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (character_x + 36) < 768-280:
        x += speed
        character_x += speed
        goes_right = True
        goes_down = False
        goes_up = False
        goes_left = False
    elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and character_x > 0:
        x -= speed
        character_x -= speed
        goes_right = False
        goes_down = False
        goes_up = False
        goes_left = True
    elif (keys[pygame.K_w] or keys[pygame.K_UP]) and character_y > 0:
        y -= speed
        character_y -= speed
        goes_right = False
        goes_down = False
        goes_up = True
        goes_left = False
    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (character_y + 56) < 633:
        y += speed
        character_y += speed
        goes_right = False
        goes_down = True
        goes_up = False
        goes_left = False
    else:
        anime = 0
    camera.update()
    camera.apply()
    drawWindow()
    

pygame.quit()
quit
