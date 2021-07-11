# 1. 몸무게가 작은 순서대로 최대 무게를 넘어기지 않게 조합한다
# 2. 구명보트를 사용하여 people 배열에서 삭제 한다
# 3. 1~2 반복한다.
def solution(people, limit):
    answer = 0
    # 몸무게가 작은 순서대로 정렬
    people.sort()
    # 최대 무게를 넘어가지 않게 조절
    while people:
        boat = 0
        count = 0
        for person in people:
            if limit >= (boat + person) and count < 2:
                boat += person
                people.remove(person)
                count += 1
            else:
                boat = 0
                count = 0
        answer += 1

    return answer


#print(solution([70, 50, 80, 50], 100))
#print(solution([70, 80, 50], 100))
print(solution([160, 150, 140, 60, 50, 40], 200) == 3)
print(solution([40, 50, 60, 90], 100) == 3) 
print(solution([70, 50, 80, 50],100) == 3)
print(solution([70, 80, 50], 100) ==3)