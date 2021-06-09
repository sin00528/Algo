k = int(input())
food_times = list(map(int, input().split()))
n = len(food_times)

def solution(food_times, k):
    k = k + 1
    answer = 0

    while k != 0:
        for idx, val in enumerate(food_times):
            if sum(food_times) == 0:
                answer = -1
                break

            if val == 0:
                continue
            else:
                answer = idx
                food_times[idx] -= 1
                k -= 1

            if k == 0:
                break

    return answer + 1

print(solution(food_times, k))