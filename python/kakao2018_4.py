def solution(food_times, k):
    answer = 0
    timeLeft = k
    minValue = 100000000
    fSet = []
    for i in range(len(food_times)):
        fSet.append([i,food_times[i]])
        if fSet[i][1] < minValue:
            minValue = fSet[i][1]
    print(fSet)
    print(minValue)

    # while answer == 0:
    #     temp = []
    #     if timeLeft > minValue*len(fSet):
    #         for x in fSet:
    #             x[1] -= minValue
    #             if x[1] == 0:
    #                 temp.append(x)
    #         timeLeft -= minValue*len(fSet)
    #         for x in temp:
    #             if x[1] < minValue:
    #                 minValue = x[1]
    #         fSet = temp
    #     else:
    #         print(fSet)
    #         answer = "test"

    return answer


test1 = [3,1,2]
test2 = 5
print(solution(test1, test2))