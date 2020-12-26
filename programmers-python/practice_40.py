def solution(A, B):
    answer = 0

    A, B = sorted(A), sorted(B)
    for i in range(len(A)):
        answer += A[i] * B[len(B) - 1 - i]

    return answer


A1 = [1, 4, 2]
B1 = [5, 4, 4]
A2 = [1, 2]
B2 = [3, 4]

print(solution(A1, B1))
print(solution(A2, B2))
