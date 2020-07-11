def solution(n):
    answer = 0

    for x in str(n):
        answer += int(x)

    return answer

print(solution(123))
print(solution(987))
