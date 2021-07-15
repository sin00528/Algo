# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부분 번호를 공백으로 구분하여 입력
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

