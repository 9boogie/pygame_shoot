import pygame
import random
#from random import *
####################################################################

#기본 초기화 (반드시 해야함)
pygame.init()  #초기화 (반드시 필요)

#화면크기 설정 
screen_width = 480   #가로
screen_height = 640   #세로 
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Jae Game")  #게임 이름 

# FPS
clock = pygame.time.Clock()

background = pygame.image.load("/Users/jaeyoungkim/lighthouse/pygame_basic/background.png")
########################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등 )
background = pygame.image.load("/Users/jaeyoungkim/lighthouse/pygame_basic/background.png")

#캐릭터 (스프라이트)  불러오기
character = pygame.image.load("/Users/jaeyoungkim/lighthouse/pygame_basic/character.png") 
character_size = character.get_rect().size   #이미지의 크기를 구해옴 
character_width = character_size[0]   #캐릭터의 가로크기
character_height = character_size[1]  #캐릭터의 세로 크기 
character_x_pos = screen_width / 2 - (character_width / 2)  #화면 가로의 절반 크기에 해당하는곳에 위치 
character_y_pos = screen_height - character_height 

#이동할 좌표 
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6 

enemy = pygame.image.load("/Users/jaeyoungkim/lighthouse/pygame_basic/enemy.png") 
enemy_size = enemy.get_rect().size   #이미지의 크기를 구해옴 
enemy_width = enemy_size[0]   #캐릭터의 가로크기
enemy_height = enemy_size[1]  #캐릭터의 세로 크기 
enemy_x_pos = random.randint(0,screen_width - enemy_width)  #화면 가로의 절반 크기에 해당하는곳에 위치 
enemy_y_pos = 0

enemy_speed = 15
  
#이벤트 루프
running = True   #게임이 진행중인가? 
while running:  
    dt = clock.tick(30)   #게임화면의 초당 프레임 수를 설정 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():      #pygame을 사용하기 위해 무조건 필요한 문장 (어떤 이벤트가 발생하였는가? )
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤트가 발생하였는가?
            running = False            #게임이 진행중이 아님 
        
        if event.type == pygame.KEYDOWN:   #키가 눌러졌는지 확인 
            if event.key == pygame.K_LEFT:   #캐릭터를 왼쪽으로
                to_x -= character_speed             
            elif event.key == pygame.K_RIGHT:     
                to_x += character_speed   
            
        
        if event.type == pygame.KEYUP:   # 방향키를 떼면 멈춤 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                        
                  
    character_x_pos += to_x * dt
    '''enemy_y_pos += 15 
    if enemy_y_pos >= 630: 
        enemy_y_pos = 0
        enemy_x_pos = randrange(0,400)'''
    
    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width - enemy_width)
    
    if character_x_pos < 0 : 
        character_x_pos = 0 
    elif character_x_pos > (screen_width - character_width) : 
        character_x_pos = (screen_width - character_width)

    #충돌 처리를 위한 rect 정보 업데이트 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요!")
        running = False
  

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,screen_height - character_height))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos)) 

    pygame.display.update()  #게임 화면을 다시 그리기! 


#pygame 종료 
pygame.quit()