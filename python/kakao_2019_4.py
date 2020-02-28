import queue

def solution(food_times, k):
    foodsQ = queue.Queue()

    for i in range(len(food_times)):
        foodsQ.put([i+1, food_times[i]])

    for i in range(k):
        if foodsQ.qsize():
            food = foodsQ.get()
            food[1] -= 1
            if food[1] == 0:
                continue
            else:
                foodsQ.put(food)
        else:
            break

    if foodsQ.qsize() == 0:
        return -1
    else:
        return foodsQ.get()[0]

# totalFoods = 0
# k = random.randrange(1000000, 1500000)
# food_times = []
# for i in range(2000):
#     foodCnt = random.randrange(500, 1000)
#     food_times.append(foodCnt)
#     totalFoods += foodCnt
#
# print(solution(food_times, k))
# print("k = ", k)
# print("totalFoods = ", totalFoods)
# print("length of food_times = ", len(food_times))
# print("food_times = ", food_times)

# print(solution([3,1,2], 5))
# print(solution([3,1,2], 6))
# print(solution([3,1,2], 7))
# print(solution([3,1,2,2], 5))