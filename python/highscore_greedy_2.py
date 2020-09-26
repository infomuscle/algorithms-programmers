from itertools import combinations


def solution(number, k):
    max = 0
    idxs = list(i for i in range(len(number)))
    combs = combinations(idxs, k)
    for c in combs:
        tmp = ""
        for i, n in enumerate(number):
            if i not in c:
                tmp += n
        if int(tmp) > max:
            max = int(tmp)

    answer = str(max)
    return answer


n1 = "1924"
k1 = 2
n2 = "1231234"
k2 = 3
n3 = "4177252841"
k3 = 4

print(solution(n1, k1))
print(solution(n2, k2))
print(solution(n3, k3))
