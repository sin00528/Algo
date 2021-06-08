n, k = map(int, input().split())
result = 0

# 반복문 불변식: n != 1 (1이 되면 종료)
while n != 1:
    # N이 K로 나누어 떨어지면 N로 나누기
    if n % k == 0:
        n = n // k
        result += 1
    # N이 K로 나누어 떨어지지 않으면 1빼기
    else:
        n -= 1
        result += 1

print(result)