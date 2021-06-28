def solution(name):
    # 아스키 코드를 이용하여 상하 이동 최소 횟수를 구함
    graph = [min(abs(ord(char) - ord('A')), abs(ord('Z') - ord(char)+1)) for char in name]
    now, answer = 0, 0
    while True:
        # 현재 방문노드 처리
        answer += graph[now]
        graph[now] = 0
        # 모든 노드를 방문하였을때 종료
        if sum(graph) == 0:
            break
        # 좌측과 우측을 비교하며 더 짧은 곳으로 이동
        left, right = 1, 1
        # 좌측 체크: 현재 문자열을 변경할 필요가 없는 경우 좌측으로 이동
        while graph[now - left] == 0:
            left += 1
        # 우측 체크: 현재 문자열을 변경할 필요가 없는 경우 우측으로 이동
        while graph[now + right] == 0:
            right += 1
        # 더 작은 값으로 업데이트 후
        # 이동 거리가 더 짧은 곳으로 인덱스를 이동
        answer += min(left, right)
        now +=  -left if left < right else right
    return answer     

#print(solution("JEROEN"))
#print(solution("JAN"))
print(solution("JEROEN")==56)
print(solution("JAN")==23)