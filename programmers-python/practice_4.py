def solution(a, b):
    answer = 0

    if b < a:
        s, e = b, a
    else:
        s, e = a, b

    for i in range((e - s + 1) // 2):
        answer += (s + e)

    if (e - s + 1) % 2 == 1:
        answer += (s + e) // 2

    return answer


a1, b1 = 3, 5
a2, b2 = 3, 3
a3, b3 = 5, 3

print(solution(a1, b1))
print(solution(a2, b2))
print(solution(a3, b3))
