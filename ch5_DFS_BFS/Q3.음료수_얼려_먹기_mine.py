n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위 벗어나는 경우
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 방문하지 않은 경우, 해당노드 방문처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)
