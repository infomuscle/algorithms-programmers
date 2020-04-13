def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False

    try:
        num = int(s)
    except:
        answer = False

    return answer

s1 = "a234"
s2 = "1234"

print(solution(s1))
print(solution(s2))