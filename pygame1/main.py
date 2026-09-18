import sys,pygame
pygame.init()
size = width, height = 1280, 720
speed = [5, 5]
black = 0,0,0
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif")
ball_rect = ball.get_rect()
class GameObject:
    def __init__(self,image,x,y,speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.pos = image.get_rect().move(self.x,self.y)
    def move(self):
        self.pos = self.pos.move(self.speed,0)
        if self.pos.right > width:
            self.pos.left = 0
ballObject = GameObject(ball,width /2, height / 2, 5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)
    ballObject.move()
    screen.blit(ballObject.image, ballObject.pos)
    pygame.display.flip()
    clock.tick(60)