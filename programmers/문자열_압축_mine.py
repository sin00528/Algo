def solution(s):
    answer = len(s)
    # step을 늘려가며 압축 문자열 길이가 최소인 step 찾기
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step] # 이전 문자열 저장
        count = 1
        # 문자열 압축 진행
        for j in range(step, len(s), step):
            # 우측에 이전 문자열과 같은 문자열이 존재할 경우
            if prev == s[j:j+step]:
                count += 1
            # 우측에 이전 문자열과 같은 문자열이 존재 하지 않을 경우
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        # 처리되지 않은 문자열 처리(끝까지 이전 문자열과 같은 문자열이 계속 이어질때)
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer
print(solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd") == 17)