# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * n for _ in range(n)]
# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

# 시뮬레이션 시작
count = 1   # 초기 위치는 자동으로 셈
turn_time = 0
while True:
    # 현재 방향을 기준으로 왼쪽 방향부터 탐색
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 갈 수 있는곳이면, 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 네 방향 모두 이미 가본칸일 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 모두 바다라 움질일 수 없을 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)