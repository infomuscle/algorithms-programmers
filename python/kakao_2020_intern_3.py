def solution(gems):
    gems_set = set(gems)
    answers = []

    p1, p2 = 0, 0
    while p1 <= len(gems):
        # print(p1, p2)
        while gems_set != set(gems[p2:p1 + 1]) and p1 != len(gems):
            p1 += 1
        right = p1

        lefts = []
        while True:
            if gems_set == set(gems[p2:right + 1]):
                lefts.append(p2)
            if p2 == right:
                if len(lefts) != 0:
                    p2 = p1
                    p1 = lefts[-1]
                break
            p2 += 1

        if len(lefts) != 0:
            answers.append([lefts[-1] + 1, right + 1])
        if p1 == p2:
            p1 += 1
            p2 += 1

    min_range = min(a[1] - a[0] for a in answers)
    min_answers = []
    for a in answers:
        if a[1] - a[0] == min_range:
            min_answers.append(a)
    answer = min_answers[0]

    return answer


g1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g2 = ["AA", "AB", "AC", "AA", "AC"]
g3 = ["XYZ", "XYZ", "XYZ"]
g4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

print(solution(g1))
print(solution(g2))
print(solution(g3))
print(solution(g4))
