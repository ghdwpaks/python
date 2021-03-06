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

class obj :
    def __init__(self) :
        self.x = 0
        self.y = 0
    def put_img(self, address) :
        if address[-3:] == 'png' :
            self.img = pygame.image.load(address).convert_alpha()#이미지
        else :
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
    def change_size(self,sx,sy) :
        self.img = pygame.transform.scale(self.img,(sx,sy))
        self.sx, self.sy = self.img.get_size()
    def show(self) :
        screen.blit(self.img,(self.x,self.y))
ss = obj()
ss.put_img("C:\workspace\py\day16\homework\weekend2\pygame\ss.png")
ss.change_size(50,50)
ss.x = (size[0] // 2) - (ss.sx // 2)
ss.y = size[1] - ss.sy - 15

#ss = pygame.image.load("C:\workspace\py\day16\homework\weekend2\pygame\ss.png").convert_alpha()#이미지
#ss = pygame.transform.scale(ss,(50,50))
#ss_sx , ss_sy = ss.get_size()#ss의 가로, 세로 크기
#ss_x = (size[0] // 2) - (ss_sx // 2)#ss의 x좌표(픽셀)위치
#ss_y = size[1] - ss_sy - 5#ss의 y 좌표(픽셀)위치
black = (0,0,0)
white = (255,255,255)
k = 0

#4.메인 이벤트
SB = 0
while SB == 0 :
    #4-1.FPS설정
    clock.tick(60)
    
    #4-2.각종 입력 감지
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: 
            SB = 1
        print("event :",event)
        print("event.type :",event.type)
    
    #4-3.입력, 시간에 따른 변화
    k += 1
    
    #4-4.그리기
    screen.fill(white)
    ss.show()
    
    #4-5.업데이트
    pygame.display.flip()

#5. 게임 종료
pygame.quit()
