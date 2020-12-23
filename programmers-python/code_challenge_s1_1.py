def solution(numbers):
    answer_set = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            answer_set.add(numbers[i] + numbers[j])
    answer = sorted(list(answer_set))

    return answer


n1 = [2, 1, 3, 4, 1]
n2 = [5, 0, 2, 7]

print(solution(n1))
print(solution(n2))
