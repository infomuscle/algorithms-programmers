def solution(n):
    answer = list(map(int, reversed(str(n))))
    return answer


n1 = 12345
print(solution(n1))
