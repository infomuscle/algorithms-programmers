from collections import OrderedDict
from collections import deque


def solution(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        return -1

    foods = OrderedDict()
    for i, ft in enumerate(food_times):
        foods[i] = ft

    time_passed = 0
    while time_passed + len(foods) < k:
        time_passed += len(foods)

        key_to_delete = []
        for fk in foods.keys():
            foods[fk] -= 1
            if foods[fk] == 0:
                key_to_delete.append(fk)

        for ktd in key_to_delete:
            del foods[ktd]

    time_left = k - time_passed
    queue = deque()
    for fk in foods.keys():
        queue.append({fk: foods[fk]})

    for i in range(time_left):
        food = queue.popleft()
        queue.append(food)

    answer = list(queue.popleft().keys())[0] + 1

    return answer


print(solution([5, 4, 3, 2, 1], 1))
print(solution([5, 4, 3, 2, 1], 2))
print(solution([5, 4, 3, 2, 1], 3))
print(solution([5, 4, 3, 2, 1], 4))
print(solution([5, 4, 3, 2, 1], 5))
print(solution([5, 4, 3, 2, 1], 6))
print(solution([5, 4, 3, 2, 1], 7))
print(solution([5, 4, 3, 2, 1], 8))
print(solution([5, 4, 3, 2, 1], 9))
print(solution([5, 4, 3, 2, 1], 10))
print(solution([5, 4, 3, 2, 1], 11))
print(solution([5, 4, 3, 2, 1], 12))
print(solution([5, 4, 3, 2, 1], 13))
print(solution([5, 4, 3, 2, 1], 14))
print(solution([5, 4, 3, 2, 1], 15))

f1 = [3, 1, 2]
k1 = 5
print(solution(f1, k1))
