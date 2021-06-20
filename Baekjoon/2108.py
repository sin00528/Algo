from collections import Counter
n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array.sort()

def calc_mean(array):
    mean = sum(array) / len(array)
    return mean

def calc_median(array):
    mid = len(array) // 2
    median = array[mid]
    return median

def calc_mode(array):
    if len(array) == 1:
        return array[0]

    candi = Counter(array).most_common(2)
    mode = candi[0][0]
    
    if candi[0][1] == candi[1][1]:
        mode = candi[1][0]
    return mode

def calc_difference(array):
    difference = abs(array[-1] - array[0])
    return difference

mean = calc_mean(array)
median = calc_median(array)
mode = calc_mode(array)
difference = calc_difference(array)

print(round(mean))
print(median)
print(mode)
print(difference)
