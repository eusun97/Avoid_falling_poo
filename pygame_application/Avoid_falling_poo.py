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


running = True
while running:
    dt = clock.tick(30)

# 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# 화면에 그리기
    screen.blit(back, (0,0))


    pygame.display.update()

pygame.quit()




