def solution(s):
    answer = ""
    s_lower = s.lower()

    is_first = True
    for sl in s_lower:
        if sl == " ":
            is_first = True
        else:
            if is_first:
                sl = sl.upper()
                is_first = False
        answer += sl

    return answer


s1 = "3people unFollowed me"
s2 = "for the last week"
s3 = "%"

print(solution(s1))
print(solution(s2))
print(solution(s3))
