def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] != " ":
            o = ord(s[i])
            e = o + n
            if (o >= 65 and o <=90 and e > 90) or (o >= 97 and o<= 122 and e > 122):
                e -= 26
            answer += chr(e)
        else:
            answer += s[i]

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("Z C", 25))