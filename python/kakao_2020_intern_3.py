def solution(gems):
    answer = []

    gems_map = dict()
    for g in gems:
        if g not in gems_map.keys():
            gems_map[g] = 0
        gems_map[g] += 1

    pl, pr = 0, len(gems) - 1

    while True:
        is_there_all_gem = True
        for g in gems_map.keys():
            if gems[pl:pr + 1].count(g) == 0:
                is_there_all_gem = False
                break
        if is_there_all_gem == True:
            pr -= 1
        else:
            pr += 1
            break

    while True:
        is_there_all_gem = True
        for g in gems_map.keys():
            if gems[pl:pr + 1].count(g) == 0:
                is_there_all_gem = False
                break
        if is_there_all_gem == True:
            pl += 1
        else:
            pl -= 1
            break

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
