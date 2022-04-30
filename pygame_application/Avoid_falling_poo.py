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


# 화면에 그리기
    screen.blit(back, (0,0))
    screen.blit(char, (char_x_pos, char_y_pos))


    pygame.display.update()

pygame.quit()




