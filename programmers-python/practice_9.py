def solution(s):
    center = len(s) // 2

    if len(s) % 2 == 0:
        answer = s[center - 1] + s[center]
    else:
        answer = s[center]

    return answer


s1 = "abcde"
s2 = "qwer"

print(solution(s1))
print(solution(s2))
