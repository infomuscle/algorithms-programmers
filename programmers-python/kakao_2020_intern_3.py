def solution(gems):
    diversity = len(set(gems))
    left = 0
    right = len(gems) - 1

    while True:
        if len(set(gems[left:right + 1])) == diversity:
            right -= 1
        else:
            right += 1
            break

    while True:
        if len(set(gems[left:right + 1])) == diversity:
            left += 1
        else:
            left -= 1
            break

    return [left + 1, right + 1]


g1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g2 = ["AA", "AB", "AC", "AA", "AC"]
g3 = ["XYZ", "XYZ", "XYZ"]
g4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
g5 = ["T"]

print(solution(g1))
print(solution(g2))
print(solution(g3))
print(solution(g4))
print(solution(g5))
