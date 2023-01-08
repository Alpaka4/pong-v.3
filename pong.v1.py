import pygame
import sys

# здесь определяются константы,
# классы и функции
FPS = 60
SCREEN_WIDTH=1920
SCREEN_HEIGHT=1000
BAT_WIDTH=20
BAT_HEIGHT=120
BAT_OFFSET=10
BAT_2_WIDTH=20
BAT_2_HEIGHT=120
BAT_2_OFFSET=10
def point_in_rect(px,py,rect_x,rect_y,rect_w,rect_h):
    inx=rect_x<=px<=rect_x+rect_w 
    iny=rect_y<=py<=rect_y+rect_h
    return inx and iny
     
# здесь происходит инициация,
# создание объектов

clock = pygame.time.Clock()
WHITE = (255, 255, 255)
ORANGE = (255,155,100)
BLACK = (0,0,0)
YELLOW = (255,180,0)
sc = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()

# радиус круга
r = 20
# координаты круга
# скрываем за левой границей
ball_x = SCREEN_WIDTH//2
# выравнивание по центру по вертикали
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x=7
ball_speed_y=6
#КООРДИНАТЫ РАКЕТКИ
bat_x=BAT_OFFSET
bat_y=(SCREEN_HEIGHT-BAT_HEIGHT)//2
#скорость ракетки
bat_speed_y=0
#КООРДИНАТЫ РАКЕТКИ №2
bat_2_x=SCREEN_WIDTH-BAT_2_OFFSET-BAT_2_WIDTH
bat_2_y=(SCREEN_HEIGHT-BAT_2_HEIGHT)//2
#скорость ракетки №2
bat_2_speed_y=0
bat_2_speed_x=0

f2 = pygame.font.SysFont('algerian', 48)
left_score = 0
right_score = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # передвигаем мяч по экарну
    ball_x+=ball_speed_x
    ball_y+=ball_speed_y
    #выход за левый кран экрана
    if ball_x <= r:
        # летел налево - полетел направо
        ball_x=SCREEN_WIDTH//2
        ball_speed_x=-ball_speed_x
        right_score+=1
        ball_speed_x-=2
        ball_speed_y-=2
    if ball_x>= SCREEN_WIDTH - r:
        #летел направо - полетел налево
        ball_x=SCREEN_WIDTH//2
        ball_speed_x= -ball_speed_x
        left_score+=1
        ball_speed_x-=2
        ball_speed_y-=2
    #выход за верхний край
    if ball_y>= SCREEN_HEIGHT - r:
        #летел наверх-полетел вниз
        ball_speed_y=-ball_speed_y
    #выход за нижний край
    if ball_y<=r:
        #летел вниз-полетел наверх
        ball_speed_y=-ball_speed_y
    #передвигаем ракетку по экрану
    bat_y+=bat_speed_y
    bat_2_y+=bat_2_speed_y

    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_w]:
        bat_speed_y+=-1
    elif keys[pygame.K_s]:
        bat_speed_y += 1
    else:
        bat_speed_y=0
    if bat_y<=0:
        bat_y = 0
    if bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
        
    if keys[pygame.K_UP]:
        bat_2_speed_y+=-1
    elif keys[pygame.K_DOWN]:
        bat_2_speed_y += 1
    else:
        bat_2_speed_y=0
    if bat_2_y<=0:
        bat_2_y = 0
    if bat_2_y >= SCREEN_HEIGHT - BAT_2_HEIGHT:
        bat_2_y = SCREEN_HEIGHT - BAT_2_HEIGHT
    
    #проверяем что мяч попал в ракетку, правая граница
    #вычесляем середины сторон квадрата, описанного вокруг мяча
    mid_leftx=ball_x-r
    mid_lefty=ball_y
     
    mid_rightx=ball_x+r
    mid_righty=ball_y
     
    mid_topx=ball_x
    mid_topy=ball_y-r
     
    mid_bottomx=ball_x
    mid_bottomy=ball_y+r
    #правая граница ракетки №1
    if point_in_rect(mid_leftx,mid_lefty,bat_x,bat_y,BAT_WIDTH,BAT_HEIGHT):
        ball_speed_x=-ball_speed_x
    #верхняя граница ракетки №1
    if point_in_rect(mid_bottomx,mid_bottomy,bat_x,bat_y,BAT_WIDTH,BAT_HEIGHT):
        ball_speed_y=-ball_speed_y 
    #нижняя граница ракетки №1
    if point_in_rect(mid_topx,mid_topy,bat_x,bat_y,BAT_WIDTH,BAT_HEIGHT):
        ball_speed_x=-ball_speed_x
    #левая граница ракетки №2    
    if point_in_rect(mid_rightx,mid_righty,bat_2_x,bat_2_y,BAT_2_WIDTH,BAT_2_HEIGHT):
        ball_speed_x=-ball_speed_x
    #верхняя граница ракетки №2
    if point_in_rect(mid_bottomx,mid_bottomy,bat_2_x,bat_2_y,BAT_2_WIDTH,BAT_2_HEIGHT):
        ball_speed_y=-ball_speed_y 
    #нижняя граница ракетки №2
    if point_in_rect(mid_topx,mid_topy,bat_2_x,bat_2_y,BAT_2_WIDTH,BAT_2_HEIGHT):
        ball_speed_x=-ball_speed_x
    #score
    score_left_text = f2.render(str(left_score), True,(YELLOW))
    score_right_text = f2.render(str(right_score), True,(YELLOW))
    # заливаем фон
    sc.fill(BLACK)
    # счетчик очков
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc, WHITE,(bat_x,bat_y,BAT_WIDTH,BAT_HEIGHT))
    pygame.draw.rect(sc, WHITE,(bat_2_x,bat_2_y,BAT_2_WIDTH,BAT_2_HEIGHT))

    # обновляем окно
    sc.blit(score_left_text, (SCREEN_WIDTH//2 -100, 10))
    sc.blit(score_right_text, (SCREEN_WIDTH//2 +100, 10))
    pygame.display.update()


    clock.tick(FPS)
