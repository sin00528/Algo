n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문을 저장할 리스트
d = [[0] * n for _ in range(m)]
# 처음에 방문한곳 처리
d[x][y] = 1

# 지도 정보를 저장할 리스트
array = []
# 지도 정보 저장
for _ in range(n):
    array.append(list(map(int, input().split())))

# 방향 정보 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시점 좌측이동 함수 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 초기 방문칸수 설정
count = 1
# 회전수 설정
turn_time = 0

# 시뮬레이션 시작
while True:
    # 1. 이동 가능한지 반시계 방향으로 체크
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 2.1. 이동 가능하면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 2.2. 이동이 불가능 하다면 다시 회전
    else:
        turn_time += 1

    # 3. 네방향 모두 이미 가본칸이면 뒤로 이동
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤쪽이 바다칸이어서 이동할수 없는경우 움직임 멈춤
        else:
            break

        turn_time = 0

print(count)