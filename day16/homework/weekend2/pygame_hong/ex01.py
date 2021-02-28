import pygame

#1. 게임 초기화
pygame.init()

#2. 게임창 옵션 설정
size = [400,900]
screen = pygame.display.set_mode(size)

title = 'My Game'
pygame.display.set_caption(title)

#3. 게임 내 필요한 설정
clock = pygame.time.Clock()
color = (1,255,1)

#4.메인 이벤트
SB = 0
i = 0
while SB == 0 :
    i += 1
    #4-1.FPS설정
    clock.tick(2)
    
    #4-2.각종 입력 감지
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: 
            SB = 1
        
    
    #4-3.입력, 시간에 따른 변화
    
    #4-4.그리기
    if i % 2 == 0 :
        screen.fill((1,255,1))
    else :
        screen.fill((1,220,1))
    #4-5.업데이트
    pygame.display.flip()

#5. 게임 종료
pygame.quit()