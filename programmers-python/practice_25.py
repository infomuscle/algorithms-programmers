def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i

    return answer


n1 = 12
n2 = 5
print(solution(n1))
print(solution(n2))
