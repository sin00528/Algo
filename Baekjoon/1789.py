n = int(input())

def solution(n):
    target = n
    count = 0
    i = 1

    # target 값을 1부터 줄여나간다
    while target != 0:
        # target이 0이면 종료
        if target == 0:
            return count
        # target이 음수면 마지막에 뺀값을 더해주기 
        if target < 0:
            count -= 1
            return count
        # target이 양수면 계속 빼주기
        if target > 0:
            target -= i
            count += 1
        
        i += 1

print(solution(n))
