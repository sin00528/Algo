from collections import deque

# 도시의 개수(N), 도로의 개수(M), 거리 정보(K), 출발 도시번호(X)
n, m, k, x = map(int, input().split())

# 인접 리스트 입력
graph = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# 최단거리 리스트(start 노드에서 부터 해당 노드 까지의)
dist = [-1] * (n+1)

def bfs(graph, dist, target, start):
    # 시작 노드 큐에 삽입
    queue = deque([start])
    # 시작노드 최단거리 초기화
    dist[start] = 0
    while queue:
        current = queue.popleft()
        # 인접 리스트를 탐색
        for next_node in graph[current]:
            # 방문하지 않은경우
            if dist[next_node] == -1:
                # 최단거리 갱신
                dist[next_node] = dist[current] + 1
                queue.append(next_node)

    # 최단 거리가 정확히 K인 도시 출력
    if target in dist:
        for i in range(1, n+1):
            if target == dist[i]:
                print(i)
    # 없을 경우 -1 출력
    else:
        print(-1)
    return

bfs(graph, dist, k, x)
