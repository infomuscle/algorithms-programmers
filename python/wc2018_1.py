def solution(skill, skill_trees):
    answer = 0

    for k in range(len(skill_trees)):
        flag = 1
        idx = -1
        check = [0]*len(skill)
        for i in range(len(skill)):
            for j in range(len(skill_trees[k])):
                if skill_trees[k][j] == skill[i]:
                    if i == 0:
                        if j > idx:
                            check[i] = 1
                            idx = j
                        else:
                            flag = 0
                            break
                    else:
                        if check[i-1] == 1 and j > idx:
                            check[i] = 1
                            idx = j
                        else:
                            flag = 0
                            break
            if flag == 0:
                break
        if flag == 1:
            answer += 1

    return answer

skill = "CBD"
skillTrees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skillTrees))