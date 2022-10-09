import pygame
from ball import Ball
from random import randint




pygame.mixer.pre_init(44100, -16, 1, 512) # важно прописать до pygame.init()
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.mixer.music.load('sounds/bird.mp3')
pygame.mixer.music.play(-1)

s_catch = pygame.mixer.Sound('sounds/catch.ogg')

BLACK = (0, 0, 0)
W, H = 1000, 570

sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60

score = pygame.image.load('images/score_fon.png').convert_alpha()
f = pygame.font.SysFont('arial', 30)






telega = pygame.image.load('images/kozak_min-removebg-preview.png').convert_alpha()
#kozak_left = pygame.transform.rotate(telega, 90).convert_alpha()
kozak_left = pygame.image.load('images/kozak_min-removebg-preview_left.png').convert_alpha()

t_rect = telega.get_rect(centerx=W//2, bottom=H-5)


# JUMP
jump_force = 20         # сила прыжка
move = jump_force + 1     # текущая вертикальная скорость
t_rect.bottom


balls_data = ({'path': 'ball_bear.png', 'score': 100},
              {'path': 'ball_fox.png', 'score': 150},
              {'path': 'ball_panda.png', 'score': 200})

balls_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for data in balls_data]

def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)

game_score = 0

def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            s_catch.play()
            game_score += ball.score
            ball.kill()
        
            

balls = pygame.sprite.Group()

bg = pygame.image.load('images/back1.jpg').convert()

kozak = telega
speed = 10
createBall(balls)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

# JUMP - start     
        elif event.type == pygame.KEYDOWN:                            # проверка какая кнопка была нажата
            # смотрим св-во key, если равно K_SPACE и доп. условие прямоугольник стоит на земле, т.е. не находится в момент прыжка
            if event.key == pygame.K_SPACE and t_rect == t_rect.bottom:
                # то скорость = -jump_force. - минус, чтоб герой двигался вверх
                move = -jump_force

        # отработка прыжка

    # проверка, если скорость движения (вертикальная скорость) меньше или равна силе прыжка
    if move <= jump_force:
        if t_rect.bottom + move < t_rect:     # можем переместить так, чтоб находился выше уровня ground, т.е. выше уровня земли. rect.bottom + move < ground. Если это так
            # то мы можем перемистить нижний уровень прямоугольника на величину move, и тогда сумма будет меньше уровня земли
            t_rect.bottom += move
            # после того как переместили нащего героя, вертикальную скорость увеличиваем на 1. Но на самом деле уменьшается скорость. Изначально отрицательная -jumpforce. Это условие необходимо  move < jump_force, чтоб move(вертикальная скорость) не превышало jump_force
            if move < jump_force:
                move += 1                   # Изначально отрицательная -jumpforce, к этой отрицательной скорости добавляем 1. Т.е. наш герой подскакивая вверх будет постепенно замедляться, а потом когда
        else:                               # когда move положительный наш герой будет опускаться вниз к земле
            t_rect.bottom = t_rect            # условие rect.bottom + move < ground не сработало, значит достиг земли
                                            # мы его просто ставим на землю
            move = jump_force + 1           # тогда наш герой дальше прыгать не будет
# JUMP - end         



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        kozak = kozak_left
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        kozak = telega
        t_rect.x += speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width



    collideBalls()
    
    sc.blit(bg, (0, 0))
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))

    balls.draw(sc)
    sc.blit(kozak, t_rect)
    
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)

