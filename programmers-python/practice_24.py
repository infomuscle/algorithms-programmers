def solution(s):
    answer = ''

    idx = 0
    for i in range(len(s)):
        if s[i] == " ":
            idx = 0
            answer += s[i]
            continue

        if idx % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        idx += 1

    return answer


s1 = "try hello world"
s2 = "test this"

print(solution(s1))
print(solution(s2))
