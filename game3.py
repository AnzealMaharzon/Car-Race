import pygame
import time
import random
import winsound
pygame.init()
start_time = time.time()
player_height=200
x=0
y=0
flag = 2
car_width = 94
lane_width = 900/3
enemy_y = -100
player_y = 400
screen_width=900
screen_height=600
enemies = [ ]
gameover=False
score = 0
winsound.PlaySound("awaj.wav",winsound.SND_ASYNC| winsound.SND_ALIAS) 
score_font=pygame.font.SysFont('agent', 30)
font_1=pygame.font.SysFont('agent', 40)
font_2=pygame.font.SysFont('agent', 30)
#background_img = pygame.image.load('road.png')
screen = pygame.display.set_mode((screen_width,screen_height))
background_img = pygame.image.load('road.png')
player_img = pygame.image.load('car.png')
enemy_img = pygame.image.load('enemy.png')
def move_background(road_x,road_y,screen_height,screen,road_img):
    rel_y=road_y%screen_height
    #print("rel_y {}".format(rel_y))
    screen.blit(road_img,(road_x,rel_y-screen_height))  
    #print("rel_y-height {}".format(rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(road_img,(x,rel_y))
    road_y+=8
    return road_y

def generate_enemies(enemy_y,lane_width,enemies,car_width):
    flag = random.randrange(1,4,1)
    enemies.append([int(flag * lane_width - (lane_width + car_width)/2),enemy_y,flag])

def enemy_moment(enemies,game_screen,sprite_img):
    if len(enemies)<=0 : return
    for enemy in enemies:
        game_screen.blit(sprite_img,(enemy[0],enemy[1]))
        enemy[1]+=7
def splice_enemies(enemies,score):
    for enemy in enemies:
        if enemy[1]>=600:
            index_enemy=enemies.index(enemy)
            enemies.pop(index_enemy)
            score+=1
            pygame.mixer.music.load("point.wav")
            pygame.mixer.music.play(0)
    return (enemies,score)

def car_thakkar(enemies,player_y,player_height,flag,gameover):
    for enemy in enemies:
        if flag==enemy[2] and enemy[1]+ player_height>=player_y:
            gameover=True
            return gameover

def gameover_screen(screen,font_1,font_2,score,score_font,highscore):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting=False
        screen.fill((0,0,0))
        gameover_message= font_1.render('Ka Barbad julaka !!',False,(255, 255, 255))
        click_to_try_again=font_2.render('Spacebar thichnu.. feri khelney vaye!!!',False,(255, 255, 255))
        score_display = score_font.render("score:  {}".format(score),False,(255,255,255))
        high_score = score_font.render("High Score:  {}".format(highscore),False,(255,255,255))
        screen.blit(gameover_message,(270,100))
        screen.blit(click_to_try_again,(170,300))
        screen.blit(score_display,(200,200))
        screen.blit(high_score,(200,250))
        pygame.display.update()

running = True
while running:  
    gameover=True if car_thakkar(enemies,player_y,player_height,flag,gameover) else False
    if gameover:
        pygame.mixer.music.load("hit.wav")
        pygame.mixer.music.play(0)
        time.sleep(0.5)
        winsound.PlaySound(None,winsound.SND_ASYNC|winsound.SND_ALIAS) 
        f=open("score.txt","r+")
        f.seek(0)
        d=f.read()
        highscore = 0 if not d else d
        if(int(highscore) <= score):
            highscore=score
            f.seek(0)
            f.write(str(score))
        gameover_screen(screen,font_1,font_2,score,score_font,highscore)
        start_time=time.time()
        enemies=[]
        x=0
        y=0
        player_x=403
        player_y=400
        enemy_y=-100
        flag=2
        score = 0
        winsound.PlaySound("awaj.wav",winsound.SND_ASYNC| winsound.SND_ALIAS) 
        gameover=False     
        time.sleep(0.5)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if flag <= 1:
                    continue
                flag-=1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if flag >= 3:
                    continue
                flag+=1 
        if event.type == pygame.KEYUP:
            pass
        player_x =int( flag * lane_width - (lane_width + car_width)/2)
    if time.time()-start_time>1:
        start_time = time.time()
        generate_enemies(enemy_y,lane_width,enemies,car_width)
    y=move_background(x,y,screen_height,screen,background_img)
    score_display = score_font.render("score:  {}".format(score),False,(255,255,255))
    screen.blit(score_display,(750,50))
    screen.blit(player_img,(player_x,player_y)) 
    enemy_moment(enemies,screen,enemy_img)
   
    pygame.display.update()
    enemies,score= splice_enemies(enemies,score)