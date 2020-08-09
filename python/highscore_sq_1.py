def solution(prices):
    answer = [0] * len(prices)

    stk = []

    for i, price in enumerate(prices):
        if len(stk) != 0 and price < stk[-1][1]:
            while len(stk) != 0:
                top = stk.pop()
                if top[1] > price:
                    answer[top[0]] = i - top[0]
                else:
                    stk.append(top)
                    break
        stk.append((i, price))

    for i in range(len(stk)):
        top = stk.pop()
        answer[top[0]] = len(prices) - 1 - top[0]

    return answer


p1 = [1, 2, 3, 2, 3]
p2 = [5, 4, 3, 3, 2]
p3 = [1, 2, 3, 4, 5]
p4 = [3, 3, 3, 2, 3]

print(solution(p1))
print(solution(p2))
print(solution(p3))
print(solution(p4))
