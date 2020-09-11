def solution(numbers, target):
    answer = 0

    mes = [[]]

    for i in range(len(numbers)):
        tmps = []
        for m in mes:
            tmp1 = m + [numbers[i]]
            tmp2 = m + [-numbers[i]]
            if tmp1 not in mes:
                tmps.append(tmp1)
            if tmp2 not in mes:
                tmps.append(tmp2)
        mes = tmps

    for m in mes:
        if sum(m) == target:
            answer += 1

    # print(mes)
    # print(len(mes))

    return answer


n1 = [1, 1, 1, 1, 1]
n2 = [1, 2, 3, 4, 5]

print(solution(n1, 3))
print(solution(n2, 3))
