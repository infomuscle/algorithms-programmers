import math


def solution(n):
    x = math.sqrt(n)

    if x == int(x):
        return int((x + 1) ** 2)
    else:
        return -1


n1 = 121
n2 = 3

print(solution(n1))
print(solution(n2))
