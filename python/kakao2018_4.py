def solution(food_times, k):
    answer = -1
    cnt = 0
    i = 0

    while True:
        if food_times[i] != 0:
            food_times[i] -= 1
            i += 1
            cnt += 1
        else:
            i += 1

        if i == len(food_times):
            i = 0

        if cnt == k:
            break

    for x in range(len(food_times)):
        if food_times[i] != 0:
            answer = i+1
            break
        else:
            i += 1
            if i == len(food_times):
                i = 0

    return answer


test1 = [3,1,2]
test2 = 5
print(solution(test1, test2))