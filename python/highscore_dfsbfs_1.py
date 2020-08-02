from itertools import permutations


def solution(numbers, target):
    answer = 0

    signs = []
    for i in range(0, len(numbers)):
        s = []
        s += ["-"] * i
        s += ["+"] * (len(numbers) - i)
        signs.append(s)

    perms = []
    for s in signs:
        temp = list(permutations(s, len(s)))
        for t in temp:
            if t not in perms:
                perms.append(t)

    for p in perms:
        s = ""
        for i in range(len(p)):
            s += p[i] + str(numbers[i])
        if eval(s) == target:
            answer += 1

    return answer


n1 = [1, 1, 1, 1, 1]
t1 = 3
print(solution(n1, t1))
