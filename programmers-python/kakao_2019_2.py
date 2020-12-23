import operator

def solution(N, stages):
    answer = []
    stepper = [0] * (N+1)
    failRates = {}

    for i in range(len(stages)):
        for j in range(stages[i]):
            stepper[j] += 1

    for i in range(len(stepper)):
        if i < len(stepper)-1:
            if stepper[i] == 0:
                failRate = 0
            else:
                failRate = (stepper[i] - stepper[i+1]) / stepper[i]
            failRates[i+1] = failRate
    sortedFr = sorted(failRates.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(len(sortedFr)):
        answer.append(sortedFr[i][0])

    return answer


print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))
print(solution(5, [6,6,6,6,6]))
print(solution(5, [3,3,3,3,3]))
