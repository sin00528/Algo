n = int(input())
array = list(map(int, input().split()))

array.sort()
min_val, max_val = array[0], array[-1]

print(min_val, max_val)