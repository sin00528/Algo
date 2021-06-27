def solution(name):
    target = [min(abs(ord(char) - ord('A')), abs(ord('Z') - ord(char)+1)) for char in name]
    idx, answer = 0, 0
    while True:
        # 현재 방문 인덱스 처리
        answer += target[idx]
        target[idx] = 0
        if sum(target) == 0:
            break
        # 좌 우 체크
        left, right = 1, 1
        # 좌측 체크
        while target[idx - left] == 0:
            left += 1
        # 우측 체크
        while target[idx + right] == 0:
            right += 1
        # 더 작은 값으로 업데이트
        answer += left if left < right else right
        # 인덱스 조정 (좌측이동, 우측이동)
        idx +=  -left if left < right else right
    return answer
        

#print(solution("JEROEN"))
#print(solution("JAN"))
print(solution("JEROEN")==56)
print(solution("JAN")==23)