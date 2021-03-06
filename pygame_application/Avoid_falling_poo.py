import random
import pygame

pygame.init()

# 게임화면 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('떨어지는 똥 피하기!')

clock = pygame.time.Clock()

# 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트, 시간 등)
# 배경 만들기
back = pygame.image.load("C:\\Pygame_application\\pygame_application\\background.png")

# 캐릭터 만들기
char = pygame.image.load('C:\\Pygame_application\\pygame_application\\character.png')
char_size = char.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x_pos = (screen_width / 2) - (char_width / 2)
char_y_pos = screen_height - char_height

# 이동 위치
to_x = 0

char_speed = 1

# 똥 만들기
poo = pygame.image.load('C:\\Pygame_application\\pygame_application\\poo.png')
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_x_pos = random.randint(0, screen_width - poo_width)
poo_y_pos = 0

poo_speed = 20

# 폰트 정의
font = pygame.font.Font(None, 55)

# 총 시간
total_time = 20

start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(30)

# 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= char_speed
            elif event.key == pygame.K_RIGHT:
                to_x += char_speed
           
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

# 게임 캐릭터 위치 정의
    char_x_pos += to_x * dt

    if char_x_pos < 0:
        char_x_pos = 0
    elif char_x_pos > screen_width - char_width:
        char_x_pos = screen_width - char_width

    poo_y_pos += poo_speed

# 똥 위치 정의
    if poo_y_pos > screen_height: # 맨밑으로 떨어졌으면
        poo_y_pos = 0 # 똥 좌표를 다시 맨위로 올림
        poo_x_pos = random.randint(0, screen_width - poo_width) # 똥을 새롭게 만들기

# 충돌 처리
    char_rect = char.get_rect()
    char_rect.left = char_x_pos
    char_rect.top = char_y_pos

    poo_rect = poo.get_rect()
    poo_rect.left = poo_x_pos
    poo_rect.top = poo_y_pos

    if char_rect.colliderect(poo_rect):
        print("-- [실패] 똥을 맞았습니다. --")
        running = False

# 화면에 그리기
    screen.blit(back, (0,0))
    screen.blit(char, (char_x_pos, char_y_pos))
    screen.blit(poo, (poo_x_pos, poo_y_pos))

# 타이머
    time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = font.render(str(int(total_time - time)), True, (0,0,0))

    screen.blit(timer, (10,10))

    if total_time - time <= 0:
        print("-- [성공] 게임을 종료합니다. --")
        running = False

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()




