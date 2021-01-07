def solution(gems):
    diversity = len(set(gems))
    left, right = 0, 0

    total_line = len(gems)
    answer = [1, total_line]
    while right < total_line:
        part_line = set(gems[left:right + 1])
        if len(part_line) < diversity:
            right += 1
        else:
            if right - left < answer[1] - answer[0]:
                answer = [left + 1, right + 1]
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
print(solution(g5))
