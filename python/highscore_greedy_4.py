from collections import deque


def solution(people, limit):
    answer = 0

    lefts = deque(enumerate(sorted(people, reverse=True)))
    while len(lefts) != 0:
        unboated = deque()
        weight_on_boat = 0
        for i in range(len(lefts)):
            p = lefts.popleft()
            if weight_on_boat + p[1] <= limit:
                weight_on_boat += p[1]
            else:
                unboated.append(p)

        lefts = unboated
        answer += 1

    return answer


p1 = [70, 50, 80, 50]
l1 = 100
p2 = [70, 80, 50]
l2 = 100

print(solution(p1, l1))
print(solution(p2, l2))
