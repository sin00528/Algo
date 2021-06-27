# 1.벽 3개 임의로 배치
# 2. 바이러스 BFS로 퍼지는것 시뮬레이션
# 3. 0 개수 세기
# 4. 1~3 반복해서 0이 가장 많은 결과 출력
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]
temps = [[0] * m for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def walls_dfs(num_walls):
    global answer
    # 벽 3개 배치 
    if num_walls == 3:
        for i in range(n):
            for j in range(m):
                temps[i][j] = data[i][j]

        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temps[i][j] == 2:
                    virus_bfs(i, j)
        # 안전영역 계산
        answer = max(answer,  get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                num_walls += 1
                walls_dfs(num_walls)
                data[i][j] = 0
                num_walls -= 1

def virus_bfs(x, y):
    queue = deque([(x, y)])
    # 현재노드 방문처리
    temps[x][y] = 2
    while queue:
        x, y = queue.popleft()
        # 인접 노드 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위에 해당하는 경우
            if (0 <= nx < n) and (0 <= ny < m):
                # 방문하지 않은 경우
                if temps[nx][ny] == 0:
                    temps[nx][ny] = 2
                    queue.append((nx, ny))

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temps[i][j] == 0:
                score += 1
    return score

walls_dfs(0)
print(answer)

#virus_bfs(1, 5)

#print(count_zeroes(mat))

#print(show_max_zeroes(mat))
