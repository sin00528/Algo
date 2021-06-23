n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위 처리
    if -1 >= x or x >= n or -1 >= y or y >= m:
        return False
    # 방문 로직
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
