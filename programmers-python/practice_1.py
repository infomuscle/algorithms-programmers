def solution(n):
    answer = "수박" * (n//2)

    if n%2 == 1:
        answer += "수"

    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(10000))