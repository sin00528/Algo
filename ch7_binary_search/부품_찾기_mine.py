def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    # 좌측 탐색
    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 우측 탐색
    else:
        return binary_search(array, target, mid+1, end)

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부분 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요총한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
