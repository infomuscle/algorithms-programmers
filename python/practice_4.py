def solution(a, b):
    answer = 0

    if b < a:
       s, e = b, a
    else:
        s, e = a, b

    for i in range(s, e+1):
        answer += i

    return answer


a1, b1 = 3,5
a2, b2 = 3,3
a3, b3 = 5,3


print(solution(a1, b1))
print(solution(a2, b2))
print(solution(a3, b3))