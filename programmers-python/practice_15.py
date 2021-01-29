def solution(n):
    answerStr = ""
    l = []
    for x in str(n):
        l.append(x)

    l.sort(reverse=True)
    for x in l:
        answerStr += x

    answer = int(answerStr)

    return answer


print(solution(118372))
