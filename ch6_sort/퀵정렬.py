array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 크기가 1이면 종료
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    # 엇갈릴때까지 수행(더이상 정렬할 필요가 없을때까지)
    while left <= right:
        # 왼쪽에서부터 pivot 보다 큰 값 탐색
        while left <= end and array[pivot] >= array[left]:
            left += 1
        # 오른쪽에서부터 pivot 보다 작은 값 탐색
        while right > start and array[pivot] <= array[right]:
            right -= 1
        # 엇갈렸다면 pivot과 right 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 그게 아니라면 left와 right 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)