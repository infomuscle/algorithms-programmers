from itertools import combinations


def solution(nums):
    answer = 0

    combs = combinations(nums, 3)

    sums = list()
    for c in combs:
        sums.append(sum(c))

    sums = sorted(sums)
    max = sums[-1]

    seive = [False, False] + [True] * (max - 1)
    for i in range(2, max + 1):
        if seive[i]:
            for j in range(i * 2, max + 1, i):
                seive[j] = False

    for s in sums:
        if seive[s]:
            answer += 1

    return answer


n1 = [1, 2, 3, 4]
n2 = [1, 2, 7, 6, 4]

print(solution(n1))
print(solution(n2))
