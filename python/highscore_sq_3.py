from collections import deque


def solution(prices):
    answer = []

    stk = []
    que = deque(prices)

    for i in range(len(prices)):
        isDown = False
        num = que.popleft()
        stk.append(num)

        # print(answer, stk, que)

        time = 0
        for j in range(len(que)):
            time += 1
            next = que.popleft()
            if num > next and isDown == False:
                isDown = True
                answer.append(time)
            que.append(next)

        if isDown == False:
            answer.append(time)

    return answer


p1 = [1, 2, 3, 2, 3]
p2 = [5, 4, 3, 3, 2]
p3 = [1, 2, 3, 4, 5]
p4 = [3, 3, 3, 2, 3]

print(solution(p1))
print(solution(p2))
print(solution(p3))
print(solution(p4))
