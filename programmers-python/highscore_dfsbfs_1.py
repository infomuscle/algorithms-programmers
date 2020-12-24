from collections import deque


def solution(numbers, target):
    answer = 0

    mes = deque([[]])
    for i in range(len(numbers)):
        tmps = []
        while len(mes) != 0:
            tmp = mes.popleft()
            tmp_plus = tmp + [numbers[i]]
            tmp_minus = tmp + [-numbers[i]]
            tmps.extend([tmp_plus, tmp_minus])

        for t in tmps:
            mes.append(t)

    while len(mes) != 0:
        e = mes.popleft()
        if sum(e) == target:
            answer += 1

    return answer


n1 = [1, 1, 1, 1, 1]
n2 = [1, 2, 3, 4, 5]
n3 = [1] * 20

print(solution(n1, 3))
print(solution(n2, 3))
print(solution(n3, 4))
