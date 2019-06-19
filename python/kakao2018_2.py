import operator

def solution(N, stages):
    answer = []
    failRates = {}
    for n in range(1, N+1):
        reaches = 0
        clears = 0
        for i in range(len(stages)):
            if stages[i] > n:
                reaches += 1
                clears += 1
            elif stages[i] == n:
                reaches += 1
        if reaches == 0:
            failRate = 0
        else:
            failRate = (reaches-clears)/reaches
        failRates[n] = failRate
        # failRates.append(failRate)

    failRates = sorted(failRates.items(), key=operator.itemgetter(1), reverse=True)
    for n in range(N):
        answer.append(failRates[n][0])

    return answer

n1 = 5
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
n2 = 4
stages2 = [4,4,4,4,4]

print(solution(n1, stages1))
print(solution(n2, stages2))

# copied = sorted(failRates)
# copied.reverse()
# for i in range(N):
#     for j in range(N):
#         if copied[i] == failRates[j]:
#             answer.append(j + 1)
#             failRates[j] = 2
#             break