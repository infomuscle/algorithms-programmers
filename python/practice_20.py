def solution(s):
    answer = ''.join(sorted(s, reverse=True))
    return answer


s1 = "Zbcdefg"
s2 = "ZbcdefG"

print(solution(s1))
print(solution(s2))
