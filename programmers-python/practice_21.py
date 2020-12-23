def solution(x, n):
    answer = []

    start = x
    for i in range(n):
        answer.append(start)
        start += x

    return answer


x1 = 2
n1 = 5
x2 = 4
n2 = 3
x3 = -4
n3 = 2

print(solution(x1, n1))
print(solution(x2, n2))
print(solution(x3, n3))
