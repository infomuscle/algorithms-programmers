def solution(budgets, M):
    answer = 0

    if sum(budgets) <= M:
        return max(budgets)

    pl = min(budgets)
    pr = max(budgets)

    while True:
        if pr < pl:
            pl, pr = pr, pl
        ceil = (pl + pr) // 2
        temp = getCeiledBudgets(budgets, ceil)

        if sum(temp) <= M:
            pl = ceil + 1
            if answer == ceil:
                break
            answer = ceil
        else:
            pr = ceil - 1

    return answer

def getCeiledBudgets(budgets, ceil):
    ceiledBudgets = []
    for b in budgets:
        if b <= ceil:
            ceiledBudgets.append(b)
        else:
            ceiledBudgets.append(ceil)
    return ceiledBudgets

tc1 = [100, 100, 100, 100, 100]
tc2 = [120, 110, 140, 150]

print(solution(tc1, 400))
# print(solution(tc2, 485))
