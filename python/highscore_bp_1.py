def solution(answers):
    answer = []
    max = 0

    for i in range(3):
        if i == 0:
            count = 0
            for j in range(len(answers)):
                if answers[j] == j%5 + 1:
                     count += 1
            max = count
            answer.append(i+1)
        elif i == 1:
            count = 0
            a = [1,3,4,5]
            idx = 0
            for j in range(len(answers)):
                if j%2 == 0:
                    if answers[j] == 2:
                        count += 1
                else:
                    if answers[j] == a[idx]:
                        count += 1
                    idx += 1
                    if idx > 3:
                        idx = 0
            if count > max:
                max = count
                answer.pop()
                answer.append(i+1)
            elif count == max:
                answer.append(i+1)
        else:
            count = 0
            a = [3,1,2,4,5]
            idx = 0
            for j in range(len(answers)):
                if answers[j] == a[idx]:
                    count += 1
                if j%2 == 1:
                    idx += 1
                    if idx > 4:
                        idx = 0
            if count > max:
                max = count
                answer.pop()
                answer.append(i+1)
            elif count == max:
                answer.append(i + 1)
    return answer


tc1 = [1,2,3,4,5]
tc2 = [1,3,2,4,2]

print(solution(tc1))
print(solution(tc2))

