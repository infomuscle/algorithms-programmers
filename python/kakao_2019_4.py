import queue, random, time

def solution(food_times, k):
    foodsQ = queue.Queue()
    for i in range(len(food_times)):
        foodsQ.put([i+1, food_times[i]])

    remainEatCnt = k
    orderedFood = [0] + sorted(food_times)
    for i in range(len(orderedFood)-1):
        minFoodCnt = orderedFood[i+1] - orderedFood[i]
        subAmount = minFoodCnt * foodsQ.qsize()
        if remainEatCnt - subAmount > 0:
            remainEatCnt -= subAmount
            for j in range(foodsQ.qsize()):
                foodsQ = queueSubtractor(foodsQ, minFoodCnt)
        else:
            break

    for i in range(remainEatCnt):
        if foodsQ.qsize():
            foodsQ = queueSubtractor(foodsQ, 1)
        else:
            break

    if foodsQ.qsize() == 0:
        return -1
    else:
        return foodsQ.get()[0]

def queueSubtractor(queue,  amount):
    food = queue.get()
    food[1] -= amount
    if food[1] == 0:
        pass
    else:
        queue.put(food)
    return queue


totalFoods = 0
k = random.randrange(1000000, 1500000)
food_times = []
for i in range(2000):
    foodCnt = random.randrange(500, 1000)
    food_times.append(foodCnt)
    totalFoods += foodCnt

start = time.time()
print(solution(food_times, k))
print("time = ", time.time() - start)
print("k = ", k)
print("totalFoods = ", totalFoods)
print("length of food_times = ", len(food_times))
print("food_times = ", food_times)

print(solution([3,1,2], 5))
print(solution([3,1,2], 6))
print(solution([3,1,2], 7))
print(solution([3,1,2,2], 5))