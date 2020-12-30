def solution(n, a, b):
    answer = 1

    tournament = [[i + 1, i + 2] for i in range(0, n, 2)]

    while True:
        match = False
        for i in range(len(tournament)):
            if a in tournament[i] and b in tournament[i]:
                match = True
                break
        if match:
            break
        tmp = []
        for i in range(0, len(tournament), 2):
            t = []
            if a in tournament[i]:
                t.append(a)
            elif b in tournament[i]:
                t.append(b)
            else:
                t.append(tournament[i][0])
            if a in tournament[i + 1]:
                t.append(a)
            elif b in tournament[i + 1]:
                t.append(b)
            else:
                t.append(tournament[i + 1][0])
            tmp.append(t)
        tournament = tmp
        answer += 1

    return answer


n1, a1, b1 = 8, 4, 7

print(solution(n1, a1, b1))
