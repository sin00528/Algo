from collections import deque

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],       # 정점 1
    [1, 7],          # 정점 2
    [1, 4, 5],       # 정점 3
    [3, 5],          # 정점 4
    [3, 4],          # 정점 5
    [7],             # 정점 6
    [2, 6, 8],       # 정점 7
    [1, 7],          # 정점 8
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1 차원 리스트)
visited = [False] * 9

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)