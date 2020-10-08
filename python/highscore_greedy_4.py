from collections import deque


def solution(people, limit):
    on_boat_sum = 0
    people_on_boat = list()
    boats = 0

    people = sorted(people, reverse=True)
    left_queue = deque(enumerate(people))

    while on_boat_sum != len(people):
        on_boat = 0
        weight_of_boat = 0
        unboated_queue = deque()
        for i in range(len(left_queue)):
            p = left_queue.popleft()
            if p[0] not in people_on_boat and weight_of_boat + p[1] <= limit:
                on_boat += 1
                people_on_boat.append(p[0])
                weight_of_boat += p[1]
            else:
                unboated_queue.append(p)

        left_queue = unboated_queue
        boats += 1
        on_boat_sum += on_boat

    return boats


p1 = [70, 50, 80, 50]
l1 = 100
p2 = [70, 80, 50]
l2 = 100

print(solution(p1, l1))
print(solution(p2, l2))
