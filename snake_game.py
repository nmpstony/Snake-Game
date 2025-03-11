from config import *
from init import Snake, Object
import pygame as pg
import random
pg.init()

score = 0
highscore = 0
dir = 'RIGHT'
live = 1
time_event=5*difficult
pause = False
screen_w, screen_h = screen_size
choice = -1
x,y = -1,-1
objects=[]


pg.display.set_caption("Snake Game")
clock = pg.time.Clock()
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont('sans',size//2)
font1 = pg.font.SysFont('sans',size)
background = pg.image.load(r'Image/background.png')
background = pg.transform.scale(background, (screen_w, screen_h))
apple_sound = pg.mixer.Sound("Sound Effect/apple.mp3")
gold_sound = pg.mixer.Sound("Sound Effect/gold.mp3")
heart_sound = pg.mixer.Sound("Sound Effect/heart.mp3")
bomb_sound = pg.mixer.Sound("Sound Effect/bomb.mp3")
snake_sound = pg.mixer.Sound("Sound Effect/snake.mp3")


#create snake
snake=Snake(pos_x=snake_infor['pos_x'], pos_y=snake_infor['pos_y'])
head_ig = pg.image.load(r'Image/snake_head.png')
head_ig = pg.transform.scale(head_ig, (size, size))
head_ig = pg.transform.rotate(head_ig, -90)
body_ig = pg.image.load(r'Image/snake_body.png')
body_ig = pg.transform.scale(body_ig, (size,size))
#create food
apple=Object(pos_x = random.randint(0,(screen_w//size-1))*size, pos_y = random.randint(1,(screen_h//size-2))*size)
apple_ig = pg.image.load(r'Image/apple.png')
apple_ig = pg.transform.scale(apple_ig, (size,size))
#create heart
#heart = Object()
heart_ig = pg.image.load(r'Image/heart.png')
heart_ig = pg.transform.scale(heart_ig, (size,size))
#create golden apple

goldenapple_ig = pg.image.load(r'Image/golden_apple.png')
goldenapple_ig = pg.transform.scale(goldenapple_ig, (size,size))
#create bomb

bomb_ig = pg.image.load(r'Image/bomb.png')
bomb_ig = pg.transform.scale(bomb_ig, (size, size))



pause_ig = pg.image.load(r'Image/pause.png')
pause_ig = pg.transform.scale(pause_ig, (min(screen_size)//2,min(screen_size)//2))
pause_hcn = pause_ig.get_rect(center = (screen_w//2,screen_h//2))

def move(dir: str):
    '''
    Hàm di chuyển rắn
    '''
    screen.blit(background,(0,0))
    if dir == 'LEFT':
        snake.move(-size, 0)
    if dir == 'RIGHT':
        snake.move(size, 0)
    if dir == 'UP':
        snake.move(0, -size)
    if dir == 'DOWN':
        snake.move(0, size)

while True:
    screen.blit(background,(0,0))
    mx,my = pg.mouse.get_pos()
    tail = [snake.body[-1]]
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            '''
            Chuyển hướng rắn khi người chơi bấm nút
            '''
            if event.key == pg.K_LEFT and dir != 'RIGHT':
                if dir == 'UP':
                    head_ig = pg.transform.rotate(head_ig,90)
                if dir == 'DOWN':
                    head_ig = pg.transform.rotate(head_ig,-90)
                dir = 'LEFT'
            if event.key == pg.K_RIGHT and dir != 'LEFT':
                if dir == 'UP':
                    head_ig = pg.transform.rotate(head_ig,-90)
                if dir == 'DOWN':
                    head_ig = pg.transform.rotate(head_ig,90)
                dir = 'RIGHT'
            if event.key == pg.K_UP and dir != 'DOWN':
                if dir == 'RIGHT':
                    head_ig = pg.transform.rotate(head_ig,90)
                if dir == 'LEFT':
                    head_ig = pg.transform.rotate(head_ig,-90)
                dir = 'UP'
            if event.key == pg.K_DOWN and dir != 'UP':
                if dir == 'RIGHT':
                    head_ig = pg.transform.rotate(head_ig,-90)
                if dir == 'LEFT':
                    head_ig = pg.transform.rotate(head_ig,90)
                dir = 'DOWN'
            '''
            Dừng game khi người chơi bấm Esc
            '''
            if event.key == pg.K_ESCAPE and not pause:
                pause = True
        '''
        Tiếp tục game khi người chơi bấm Resume ở màn hình Pause
        '''
        if pause and event.type == pg.MOUSEBUTTONDOWN and (screen_w//2 - screen_w*3//20) < mx < (screen_w//2 + screen_w*3//20) and screen_h//2 < my <= (screen_h//2 + screen_h*2//30):
            pause = False
            pg.time.wait(2000)

    if not pause:
        move(dir)
    '''
    Kiểm tra va chạm với viền màn hình
    '''
    if snake.body[0][0] == -size: snake.body[0][0] = screen_w - size
    if snake.body[0][0] == screen_w: snake.body[0][0] = 0
    if snake.body[0][1] == 0: snake.body[0][1] = screen_h - size
    if snake.body[0][1] == screen_h: snake.body[0][1] = size
    '''
    Kiểm tra đầu rắn va chạm với thân
    '''
    if snake.body[0] in snake.body[3:]:
        snake_sound.play()
        live -= 1
        score -= 50
        text_point = font1.render(f'-50P', True, color['WHITE'])
        screen.blit(text_point, (snake.body[0][0], snake.body[0][1] - 2*size))
        text_point = font1.render(f'-1LIVE', True, color['WHITE'])
        screen.blit(text_point, (snake.body[0][0], snake.body[0][1] - size))
        for i in range(len(snake.body)):
            head_ig = pg.image.load(r'Image/snake_head.png')
            head_ig = pg.transform.scale(head_ig, (size, size))
            head_ig = pg.transform.rotate(head_ig, -90)
            snake.body[i] = [snake_infor['pos_x'], snake_infor['pos_y']]
        dir = 'RIGHT'
    '''
    Kết thúc game và ghi điểm cao nhất
    '''
    if live <= 0:
        pause = True
        head_ig = pg.image.load(r'Image/snake_head.png')
        head_ig = pg.transform.scale(head_ig, (size, size))
        head_ig = pg.transform.rotate(head_ig, -90)
        if score > highscore:
            highscore = score
        score = 0
        live = 1
        snake.body=[[0,size]]
        dir = 'RIGHT'
    '''
    Vẽ rắn lên màn hình
    '''
    for i in range(len(snake.body)):
        if i == 0:
            screen.blit(head_ig, (snake.body[i]))
        else:
            screen.blit(body_ig, (snake.body[i]))

    if snake.body[0][0] == apple.pos_x and snake.body[0][1] == apple.pos_y:
        '''
        Hành vi khi ăn apple
        '''
        apple_sound.play()
        score += 25
        snake.body += tail
        text_point = font1.render(f'+25P', True, color['WHITE'])
        screen.blit(text_point, (apple.pos_x, apple.pos_y - size))
        while True:
            xa,ya = random.randint(0,(screen_w//size-1))*size, random.randint(1,(screen_h//size-2))*size
            if [xa,ya] not in snake.body:
                apple.pos_x=xa
                apple.pos_y=ya
                break

    #Đếm ngược để xuất hiện event object
    if time_event >= 0 and not pause:
        time_event-=1
    if time_event ==0:
        time_event = random.randint(2*difficult,4*difficult)
        choice = random.randint(1,10)
        while True:
            x1,y1 = random.randint(0,(screen_w//size-1))*size, random.randint(1,(screen_h//size-2))*size
            if ([x1,y1] not in snake.body) and (x1!=apple.pos_x and y1 != apple.pos_y) and (x1 != x and y1 != y):
                x,y = x1,y1
                break

        #Khởi tạo special food theo tỷ lệ
        oneobject = Object()
        oneobject.pos_x, oneobject.pos_y = x,y
        if 1<= choice <= 2:     #Heart Spawn
            oneobject.type = 'heart'
            oneobject.time = 5*difficult
        elif 3 <= choice <= 6:  #Golden Apple Spawn
            oneobject.type = 'gold'
            oneobject.time = 4*difficult
        elif 7 <= choice <= 10: #Bomb Spawn
            oneobject.type = 'bomb'
            oneobject.time = 6*difficult
        objects.append(oneobject)
        choice =-1
    for index, i in enumerate(objects):
        '''
        Vẽ special food lên màn hình
        '''
        if i.time>=0: 
            if i.type == 'heart':
                '''
                Vẽ heart
                '''
                text_heart=font.render(f'{i.time}', True, color['WHITE'])
                screen.blit(heart_ig, (i.pos_x, i.pos_y))
                screen.blit(text_heart, (i.pos_x, i.pos_y))
                if snake.body[0][0] == i.pos_x and snake.body[0][1] == i.pos_y:
                    '''
                    Kiểm tra va chạm
                    '''
                    heart_sound.play()
                    live += 1
                    text_point = font1.render(f'+1 LIVE', True, color['WHITE'])
                    screen.blit(text_point, (i.pos_x, i.pos_y - size))
                    objects.pop(index)

            elif i.type == 'gold':
                '''
                Vẽ gold
                '''
                text_gold=font.render(f'{i.time}', True, color['WHITE'])
                screen.blit(goldenapple_ig, (i.pos_x, i.pos_y))
                screen.blit(text_gold, (i.pos_x, i.pos_y))
                if snake.body[0][0] == i.pos_x and snake.body[0][1] == i.pos_y:
                    '''
                    Kiểm tra va chạm
                    '''
                    gold_sound.play()
                    score += 50
                    text_point = font1.render(f'+50P', True, color['WHITE'])
                    screen.blit(text_point, (i.pos_x, i.pos_y - size))
                    objects.pop(index)
            elif i.type == 'bomb':
                '''
                Vẽ bomb
                '''
                text_bomb=font.render(f'{i.time}', True, color['WHITE'])
                screen.blit(bomb_ig, (i.pos_x, i.pos_y))
                screen.blit(text_bomb, (i.pos_x, i.pos_y))
                if snake.body[0][0] == i.pos_x and snake.body[0][1] == i.pos_y:
                    '''
                    Kiểm tra va chạm
                    '''
                    bomb_sound.play()
                    if len(snake.body) >3:
                        for _ in range(0,3): snake.body.pop()
                        text_point = font1.render(f'-3LENGTH', True, color['WHITE'])
                        screen.blit(text_point, (i.pos_x, i.pos_y - size))
                    else:
                        live -= (4 - len(snake.body))
                        text_point = font1.render(f'-{4 - len(snake.body)}LIVE', True, color['WHITE'])
                        screen.blit(text_point, (i.pos_x, i.pos_y - size))
                        snake.body = [[snake.body[0][0], snake.body[0][1]]]
                    score -= 50
                    text_point = font1.render(f'-50P', True, color['WHITE'])
                    screen.blit(text_point, (i.pos_x, i.pos_y - 2*size))
                    objects.pop(index)
                    
            i.time-=1
            
        elif i.time == 0:
            objects.pop(index)

    text_score = font.render(f'Score: {score}', True, color['WHITE'])
    screen.blit(text_score, (screen_w//2-size, size//5))
    text_highscore = font.render(f'HighestScore: {highscore}', True, color['WHITE'])
    screen.blit(text_highscore, (screen_w*2//3, size//5))
    text_live = font.render(f'Lives: {live}', True, color['WHITE'])
    screen.blit(text_live, (size//5,size//5))
    screen.blit(apple_ig, (apple.pos_x, apple.pos_y))
    if pause:
        screen.blit(pause_ig, pause_hcn)

        
    pg.display.update()
    clock.tick(difficult)