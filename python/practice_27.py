def solution(x):
    answer = True

    xs = str(x)
    sum = 0
    for s in xs:
        sum += int(s)

    if x % sum != 0:
        answer = False

    return answer


x1 = 10
x2 = 12
x3 = 11
x4 = 13

print(solution(x1))
print(solution(x2))
print(solution(x3))
print(solution(x4))
