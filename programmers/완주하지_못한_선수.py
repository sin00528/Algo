def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)

    return participant[0]


# collections 사용
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]