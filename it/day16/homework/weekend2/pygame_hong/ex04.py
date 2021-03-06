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
#b = obj
ss.put_img("C:\workspace\py\day16\homework\weekend2\pygame\ss.png")
#b.put_img("C:\workspace\py\day16\homework\weekend2\pygame\b.png")
ss.change_size(50,50)
ss.x = (size[0] // 2) - (ss.sx // 2)
ss.y = size[1] - ss.sy - 15
ss.move = 10 #우주선이 움직이는 속도

#ss = pygame.image.load("C:\workspace\py\day16\homework\weekend2\pygame\ss.png").convert_alpha()#이미지
#ss = pygame.transform.scale(ss,(50,50))
#ss_sx , ss_sy = ss.get_size()#ss의 가로, 세로 크기
#ss_x = (size[0] // 2) - (ss_sx // 2)#ss의 x좌표(픽셀)위치
#ss_y = size[1] - ss_sy - 5#ss의 y 좌표(픽셀)위치
m_list = []
d_list = []
black = (0,0,0)
white = (255,255,255)
k = 0
left_go = False
right_go = False
space_go = False
#4.메인 이벤트
SB = 0

while SB == 0 :
    #4-1.FPS설정
    clock.tick(16)
    
    #4-2.각종 입력 감지
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: 
            SB = 1
        #print("event :",event)
        #print("event.type :",event.type) 
        #print("pygame.keydown :",pygame.KEYDOWN)
        if  event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                left_go = True
            elif event.key == pygame.K_RIGHT :
                #print("\n\n오른쪽 키가 눌렸습니다!\n\n")
                right_go = True
            elif event.key == pygame.K_SPACE :
                space_go = True
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT :
                left_go = False
            elif event.key == pygame.K_RIGHT :
                right_go = False
            elif event.key == pygame.K_SPACE :
                space_go = False
    #4-3.입력, 시간에 따른 변화
    k += 1
    
    if left_go:
        ss.x -= ss.move
        if ss.x <= 0 :
            ss.x = 0
    elif right_go:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx :
            ss.x = size[0] - ss.sx
    if space_go:
        '''
        이게 미사일이 여러개여서. 여기있는 곳에서 Space 입력 받음에 따라
        미사일들을 배열에 담아주는곳입니다.
        JSP의 getter setter같은거임
        '''
        mm = obj()
        mm.put_img("C:\workspace\py\day16\homework\weekend2\pygame\mm.png")
        mm.change_size(25,25)
        #mm.x = ss.x//2 - mm.size[0]//2
        mm.x = ss.x + ss.sx//2 - mm.sx//2
        mm.y = ss.y - mm.sy - 10
        mm.move = 3 #총알이 움직이는 속도
        m_list.append(mm)
    '''
    실행해보면 이게 총알 객체가 하나밖에 안나오게 된다.
    스페이스를 눌러 총알을 발사하고 얼마 안돼 다시 발사하게 되면
    원래 발사됐던 총알은 멈추고 다른 총알이 전진하게 된다.
    '''
    for i in range(len(m_list)) :
        m = m_list[i]
        mm.y -= mm.move
        if mm.y <= -mm.sy :
            d_list.append(i)
    '''
    이유는 이 위에 있는 구문들 때문인데,
    getter setter 비스무리한거 해서
    m_list에 넣어줬더니만
    m_list에 있는걸 쓰는게 아니라
    그 앞에서 만들던걸 뺏어오는거다.

    그런데도 총알이 멈춰서 남아있는 이유는
    1.  이 위에 있는 for문으로 위치를 업데이트 시켜서 전진하는것처럼 보이게 해야하는데
        for문에서는 m_list안에 있는 값들 말고 mm 값을 건드리기 때문에 더이상 for 문의 관할을
        벗어나게 돼버린다. 그래서 위치 업데이트가 안돼서 멈춰있었던것.
    2.  m_list는 생성하고, 전진하는듯이 위치를 업데이트 시켜주는 역할이다. 만들어주는것까지
        했으니 나중에 사라지든 말든 m_list입장에서는 알바가 아니기 때문에 총알이 
        남아있었던것이다.
    '''
    
    
    #4-4.그리기
    screen.fill(white)
    ss.show()
    for m in m_list :
        m.show()
    
    #4-5.업데이트
    pygame.display.flip()

#5. 게임 종료
pygame.quit()
