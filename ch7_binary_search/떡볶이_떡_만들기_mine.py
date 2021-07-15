# 잘못된 풀이
n, m = 4, 6
arr = [19, 15, 10, 17]
# 정렬하기
arr.sort()

def solution(arr, m, start, end):
    # 높이를 이진 탐색한다
    if start > end:
        return None
    # 초기 높이를 설정
    mid = (start + end) // 2
    h = arr[mid]
    # 오른쪽의 떡길이 계산
    dduck_len = sum(arr[mid+1:]) - h * len(arr[mid+1:])

    # 길이가 일치하면 return
    if dduck_len == m:
        return h
    # 길이가 모자라면 높이를 낮추고
    elif dduck_len < m:
        solution(arr, m, start, mid-1)
    # 길이가 충분하면 높이를 높인다
    else:
        solution(arr, m, mid+1, end)

print(solution(arr, m, 0, 3))