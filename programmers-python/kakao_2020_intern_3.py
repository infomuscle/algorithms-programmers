def solution(gems):
    diversity = len(set(gems))
    left, right = 0, 0

    answer = [1, len(gems)]
    while right < len(gems):
        line = set(gems[left:right + 1])
        if len(line) < diversity:
            right += 1
        else:
            tmp = [left + 1, right + 1]
            if tmp[1] - tmp[0] < answer[1] - answer[0]:
                answer = tmp
            left += 1

    return answer


g1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g2 = ["AA", "AB", "AC", "AA", "AC"]
g3 = ["XYZ", "XYZ", "XYZ"]
g4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
g5 = ["T"]

print(solution(g1))
print(solution(g2))
print(solution(g3))
print(solution(g4))
# print(solution(g5))
