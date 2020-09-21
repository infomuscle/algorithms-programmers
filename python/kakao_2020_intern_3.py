def solution(gems):
    answer = []

    gems_set = set(gems)

    pl, pr = 0, len(gems_set) - 1

    step = 0
    while True:
        gems_tmp = gems[pl:pr + 1]
        if gems_set == set(gems_tmp):
            break
        else:
            pl += 1
            pr += 1
            if pr == len(gems):
                step += 1
                pl = 0
                pr = len(gems_set) - 1 + step

    answer.append(pl + 1)
    answer.append(pr + 1)

    return answer


g1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g2 = ["AA", "AB", "AC", "AA", "AC"]
g3 = ["XYZ", "XYZ", "XYZ"]
g4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

print(solution(g1))
print(solution(g2))
print(solution(g3))
print(solution(g4))
