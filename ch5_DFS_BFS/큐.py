from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용 : O(1)
# 리스트 자료형을 이용하는 경우, 시간 복잡도가 더 높아서 비효율적임
# 리스트로 구현 하여 원소를 pop으로 빼내는 연산을 수행할 경우 : O(K)
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력

