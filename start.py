import random
import msvcrt

# 게임 화면 크기 설정
WIDTH = 20
HEIGHT = 10

# 지렁이 초기 위치 및 방향 설정
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
direction = 'RIGHT'

# 먹이 위치 설정
food_x = random.randint(0, WIDTH - 1)
food_y = random.randint(0, HEIGHT - 1)

# 게임 루프
while True:
    # 화면 지우기
    print("\033[H\033[J", end='')

    # 게임 화면 그리기
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == snake_x and y == snake_y:
                print('O', end='')
            elif x == food_x and y == food_y:
                print('*', end='')
            else:
                print('.', end='')
        print()

    # 사용자 입력 받기
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').upper()
        if key == 'W':
            direction = 'UP'
        elif key == 'S':
            direction = 'DOWN'
        elif key == 'A':
            direction = 'LEFT'
        elif key == 'D':
            direction = 'RIGHT'

    # 지렁이 이동
    if direction == 'UP':
        snake_y -= 1
    elif direction == 'DOWN':
        snake_y += 1
    elif direction == 'LEFT':
        snake_x -= 1
    elif direction == 'RIGHT':
        snake_x += 1

    # 벽 충돌 검사
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        print("게임 오버!")
        break

    # 먹이 먹기
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, WIDTH - 1)
        food_y = random.randint(0, HEIGHT - 1)

# 게임 종료 메시지 출력
print("게임 종료")
