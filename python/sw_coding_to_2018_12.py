def solution(d, budget):
    answer = 0

    department = sorted(d)

    sum = 0
    for request in department:
        if sum + request <= budget:
            sum += request
            answer += 1
        if sum == budget:
            break
    return answer


d1 = [1, 3, 2, 5, 4]
b1 = 9
d2 = [2, 2, 3, 3]
b2 = 10

print(solution(d1, b1))
print(solution(d2, b2))
