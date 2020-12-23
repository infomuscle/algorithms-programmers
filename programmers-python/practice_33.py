def solution(n):
    answer = 0

    for i in range(1, n + 1):
        sum, adder = 0, i
        while sum < n:
            sum += adder
            adder += 1
        if sum == n:
            answer += 1

    return answer


n1 = 15
n2 = 10000

print(solution(n1))
print(solution(n2))
