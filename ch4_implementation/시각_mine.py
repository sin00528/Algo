n = int(input())

result = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있는경우, 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)