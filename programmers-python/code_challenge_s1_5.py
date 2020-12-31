def solution(n):
    return decimal(ternary(n)[::-1])


def ternary(n):
    t = ""
    while n > 0:
        t += str(n % 3)
        n //= 3

    return t[::-1]


def decimal(num: str):
    d = 0
    num = num[::-1]
    for i, n in enumerate(num):
        d += int(n) * (3 ** i)

    return d


n1 = 45
n2 = 125

print(solution(n1))
print(solution(n2))
