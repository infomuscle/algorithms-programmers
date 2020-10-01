def solution(n):
    seive = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if seive[i]:
            for j in range(i * 2, n + 1, i):
                seive[j] = False

    return seive.count(True)


n1 = 10
n2 = 5
n3 = 1000000

print(solution(n1))
print(solution(n2))
print(solution(n3))
