# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
data = []

# 한 줄씩 입력받기
for i in range(n):
    data.append(list(map(int, input().split())))

max_val = -1
for i in range(n):
    # 현재 줄에서 '가장 작은 수' 찾기
    min_val = 987654321
    for j in range(m):
        if min_val > data[i][j]:
            min_val = data[i][j]
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    if max_val < min_val:
        max_val = min_val

print(max_val)
