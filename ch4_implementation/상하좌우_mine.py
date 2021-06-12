n = int(input())
plans = input().split()

# 초기 좌표
x = 1
y = 1

# 방향 벡터 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

move_types = ['U', 'D', 'L', 'R']

for plan in plans:
    nx, ny = -1, -1
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx > n or nx < 1 or ny > n or ny < 1 :
        continue
    
    x, y = nx, ny

print(x, y)
