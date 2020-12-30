from itertools import combinations


def solution(nums):
    answer = 0

    combs = combinations(nums, len(nums) // 2)
    for comb in combs:
        diversity = len(set(comb))
        if diversity > answer:
            answer = diversity

    return answer


n1 = [3, 1, 2, 3]
n2 = [3, 3, 3, 2, 2, 4]
n3 = [3, 3, 3, 2, 2, 2]

print(solution(n1))
print(solution(n2))
print(solution(n3))
