def solution(n):
    # answer = fibonacci(n)
    answer = fibonacci(n) % 1234567
    return answer


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# print(solution(0))
# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))
# print(solution(5))
# print(solution(6))
# print(solution(7))
# print(solution(8))
# print(solution(9))
print(solution(100))
