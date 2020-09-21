def solution(gems):
    answer = []

    gems_set = set(gems)

    p1, p2 = 0, 0

    while True:
        gems_tmp = gems[:p1 + 1]
        if gems_set == set(gems_tmp):
            break
        else:
            p1 += 1

    while True:
        gems_tmp = gems[p2:p1 + 1]
        if gems_set != set(gems_tmp):
            p2 -= 1
            break
        else:
            p2 += 1

    answer.append(p2 + 1)
    answer.append(p1 + 1)

    return answer


g1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g2 = ["AA", "AB", "AC", "AA", "AC"]
g3 = ["XYZ", "XYZ", "XYZ"]
g4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

print(solution(g1))
print(solution(g2))
print(solution(g3))
print(solution(g4))
