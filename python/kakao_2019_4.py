from queue import PriorityQueue
from queue import Queue
import random, time


def solution(food_times, k):

    totalFoodAmt = 0

    pFoodsQ = PriorityQueue()
    for i in range(len(food_times)):
        pFoodsQ.put((food_times[i], i+1))
        totalFoodAmt += food_times[i]

    if k >= totalFoodAmt:
        return -1

    remainEatCnt = k
    eatenAmt = 0
    while pFoodsQ.qsize():
        food = pFoodsQ.get()
        # print(food)
        subAmt = (pFoodsQ.qsize()+1) * (food[0]-eatenAmt)
        # print(remainEatCnt)
        if remainEatCnt - subAmt > 0:
            remainEatCnt -= subAmt
            eatenAmt += food[0] - eatenAmt
        else:
            if pFoodsQ.qsize():
                pFoodsQ.put(food)
            break

    foodList = []
    while pFoodsQ.qsize():
        food = pFoodsQ.get()
        foodList.append([food[1], food[0]-eatenAmt])
    foodList = sorted(foodList)
    # print(remainEatCnt)

    nFoodsQ = Queue()
    for i in range(len(foodList)):
        nFoodsQ.put(foodList[i])
        # print(foodList[i])

    for i in range(remainEatCnt):
        if nFoodsQ.qsize():
            food = nFoodsQ.get()
            food[1] -= 1
            if food[1] > 0:
                nFoodsQ.put(food)
            else:
                continue
        else:
            return -1

    if nFoodsQ.qsize():
        answer = nFoodsQ.get()[0]
    else:
        answer = -1

    return answer

print(solution([5,4,3,2,1], 1))
print(solution([5,4,3,2,1], 2))
print(solution([5,4,3,2,1], 3))
print(solution([5,4,3,2,1], 4))
print(solution([5,4,3,2,1], 5))
print(solution([5,4,3,2,1], 6))
print(solution([5,4,3,2,1], 7))
print(solution([5,4,3,2,1], 8))
print(solution([5,4,3,2,1], 9))
print(solution([5,4,3,2,1], 10))
print(solution([5,4,3,2,1], 11))
print(solution([5,4,3,2,1], 12))
print(solution([5,4,3,2,1], 13))
print(solution([5,4,3,2,1], 14))
print(solution([5,4,3,2,1], 15))