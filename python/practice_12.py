def solution(arr, divisor):
    answer = []

    for a in arr:
        if a%divisor == 0:
            answer.append(a)

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)

arr1 = [5,9,7,10]
d1 =5
arr2 = [2,36,1,3]
d2 = 1
arr3 = [3,2,6]
d3 = 10

print(solution(arr1, d1))
print(solution(arr2, d2))
print(solution(arr3, d3))
