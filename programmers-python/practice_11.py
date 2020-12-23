def solution(arr):
    answer = []

    if len(arr) == 1:
        answer.append(-1)
        return answer

    t = sorted(arr)
    min = t[0]

    for i in range(len(arr)):
        if arr[i] != min:
            answer.append(arr[i])

    return answer