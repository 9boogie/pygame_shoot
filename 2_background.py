import pygame

pygame.init()  #초기화 (반드시 필요)

#화면크기 설정 
screen_width = 480   #가로
screen_height = 640   #세로 
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Jae Game")  #게임 이름 

#배경 이미지 불러오기 
background = pygame.image.load("C:/Users/young/OneDrive/바탕 화면/PythonWorkSpace/pygame_basic/background.png")  
# path에서 \ 를 \\ 또는 / 로 전환 그리고 "" 를 붙여준다 

#이벤트 루프
running = True   #게임이 진행중인가? 
while running:  
    for event in pygame.event.get():      #pygame을 사용하기 위해 무조건 필요한 문장 (어떤 이벤트가 발생하였는가? )
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤트가 발생하였는가?
            running = False            #게임이 진행중이 아님 
    
    #screen.fill((0,100,150))   # (red,green,blue) 색상으로 화면 채우기 
    screen.blit(background,(0,0)) # 배경 그리기 (창에서 맨위가 0,0 이다 )

    pygame.display.update()  #게임 화면을 다시 그리기! 

#pygame 종료 
pygame.quit()