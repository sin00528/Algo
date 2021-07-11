from collections import deque
n, m, v = map(int, input().split())

visited = [False] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]

# 인접 행렬 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 
    graph[b][a] = 1

def dfs(graph, start, visited):
    # 현재 방문 노드 처리
    visited[start] = True
    print(start, end=' ')
    # 인접 노드 탐색
    for next_node, value in enumerate(graph[start]):
        if value == 1:
            if not visited[next_node]:
                dfs(graph, next_node, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        # 현재 방문 노드 처리
        now = queue.popleft()
        print(now, end=' ')
        for next_node, value in enumerate(graph[now]):
            if value == 1:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)