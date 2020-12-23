def solution(s):
    answer = True

    s = s.lower()
    if s.count("p") != s.count("y"):
        answer = False

    return answer


s1 = "pPoooyY"
s2 = "Pyy"

print(solution(s1))
print(solution(s2))