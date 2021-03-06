def solution(n):
    return fibonacci(n) % 1234567


def fibonacci(n):
    fibonaccis = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n - 1):
            fibonaccis.append(fibonaccis[-1] + fibonaccis[-2])

    return fibonaccis[-1]


print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(100))
print(solution(100000))
