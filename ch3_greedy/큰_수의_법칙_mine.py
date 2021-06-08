# N, M, K를 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))
result = 0 # @result: 결과값을 저장할 변수
count = 0  # @count: 현재 횟수를 저장할 변수

# 입력받은 수를 내림차순으로 정렬하기
data.sort(reverse=True)

while True:
    for i in range(k):   # 가장 큰 수를 K 번 더하기
        if count == m:   # m번 만큼 반복하였다면 반복문 탈출
            break
        result += data[0]
        count += 1       # 더할때마다 count값 증가
    
    if count == m:       # m번 만큼 반복하였다면 반복문 탈출
        break
        
    result += data[1]
    count += 1           # 더할때마다 count값 증가

# 결과 출력
print(result)