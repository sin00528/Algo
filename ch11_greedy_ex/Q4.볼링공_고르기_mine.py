n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

count = 0
for i in range(n):
    for j in range(i+1, n):
        if data[i] == data[j]:
            continue
        else:
            count += 1

print(count)