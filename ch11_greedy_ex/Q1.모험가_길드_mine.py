n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if i <= count:
        count = 0
        result += 1

print(result)