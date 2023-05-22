import time
import pygame
import random
pygame.init()
x=0
enemies=[]
enemy_y=-400
start_time= time.time()
y=0
screen_height=600  
screen_width=900
flag=2
player_width=94
lane_width=900/3
screen = pygame.display.set_mode((screen_width,screen_height))
background_image = pygame.image.load("road.png")
playerimg = pygame.image.load("car.png")
enemyimg = pygame.image.load("enemy.png")
playery = 400
running = True;
def generate_enemies(enemy_y,lanewidth,enemies,playerwidth):
    flag = random.randrange(1,4,1)
    enemies.append[(int(flag*lane_width-(lane_width+player_width)/2),enemy_y,flag)]

def enemy_movement(enemies,screen,enemyimg):
    if len(enemies)<=0: 
        return
    for enemy in enemies:
        game_screen.blit(enemyimg,(enemy[0],enemy[3]))
        ememy[1]+=1
        

def get_movement(roadx,y,screen,tasbir,dusman,screen_height):
    pass
    rel_y=y%screen_height
    screen.blit(background_image,(x,rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(background_image,(x,rel_y))
        screen.blit(enemyimg,(100,rel_y)) 
    y=y+6
    return y


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                if flag<=1: continue
                flag-=1
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                if flag>=3: continue
                flag+=1
        
        if event.type==pygame.KEYUP:
            pass
        playerX= flag*lane_width-(lane_width+player_width)/2

        if time.time()-start_time>3:
            start_time=time.time()
            generate_enemies(enemy_y,lane_width,enemies,player_width)
    
    y = get_movement(x,y,screen,background_image,enemyimg,screen_height)
    
    screen.blit(playerimg,(playerX,playery))
    enemy_movement(enemies,screen,enemyimg)

    second_elapsed = int( time.time() - start_time)
    if second_elapsed == 3:
        start_time = time.time()

    
    pygame.display.update()
