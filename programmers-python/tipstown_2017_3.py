def solution(n, a, b):
    tournament = [[i + 1, i + 2] for i in range(0, n, 2)]

    round = 1
    while [a, b] not in tournament and [b, a] not in tournament:
        tmp = []
        for i in range(0, len(tournament), 2):
            match = []
            if a in tournament[i] or b in tournament[i]:
                match.append(list(filter(lambda x: x == a or x == b, tournament[i]))[0])
            else:
                match.append(tournament[i][0])
            if a in tournament[i + 1] or b in tournament[i + 1]:
                match.append(list(filter(lambda x: x == a or x == b, tournament[i + 1]))[0])
            else:
                match.append(tournament[i + 1][0])
            tmp.append(match)
        tournament = tmp
        round += 1

    return round


n1, a1, b1 = 8, 4, 7

print(solution(n1, a1, b1))
