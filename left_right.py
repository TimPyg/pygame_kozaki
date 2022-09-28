import pygame, sys
from pygame.locals import *




pygame.init()
speed = 30
speedControl = pygame.time.Clock()

# setup window
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Animation')

white = (255, 255, 255)
black = (0, 0,0 )

kozak_img_right = pygame.image.load('images/kozak_min-removebg-preview.png')
kozak_img_left = pygame.image.load('images/kozak_min-removebg-preview_left.png')

x=10
y=10
direction='right'


# Game Loop
while True:
    screen.fill(white)
    if direction == "right":
        x += 5
        screen.blit(kozak_img_right, (x,300))
        if x == 800:
            direction = "left"

    elif direction == "left":
        x -= 5
        screen.blit(kozak_img_left, (x,290))
        if x == 10:
            direction = 'right'
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    speedControl.tick(speed)
    
    

