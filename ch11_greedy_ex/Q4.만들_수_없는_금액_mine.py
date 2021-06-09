from itertools import combinations

n = int(input())
data = list(map(int, input().split()))
data.sort()

arr = []
sum_list = []
for i in range(1, n+1):
    arr = list(combinations(data, i))
    for j in arr:
        sum_list.append(sum(j))

sum_list.sort()
sum_list = list(set(sum_list))

result = 0
for i in sum_list:
    result += 1
    if i != result:
        break

print(result)