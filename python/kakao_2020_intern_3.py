def solution(gems):
    gems_set = set(gems)

    min_length = len(gems_set)
    max_length = len(gems)

    current_length = (min_length + max_length) // 2
    pl, pr = 0, current_length - 1

    possibles = []
    while True:
        if gems_set == set(gems[pl:pr + 1]):
            possibles.append([pl + 1, pr + 1])
            max_length = pr - pl + 1 - 1
            if (min_length + max_length) // 2 == current_length:
                break
            else:
                current_length = (min_length + max_length) // 2
            pl, pr = 0, current_length - 1
        else:
            pl += 1
            pr += 1
            if pr == len(gems):
                min_length = pr - pl + 1 + 1
                if (min_length + max_length) // 2 == current_length:
                    break
                else:
                    current_length = (min_length + max_length) // 2
                pl, pr = 0, current_length - 1

    answer = possibles[-1]
    return answer


g1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g2 = ["AA", "AB", "AC", "AA", "AC"]
g3 = ["XYZ", "XYZ", "XYZ"]
g4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

print(solution(g1))
print(solution(g2))
print(solution(g3))
print(solution(g4))
