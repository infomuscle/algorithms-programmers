def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])

        answer.append(temp)

    return answer


a11 = [[1, 2], [2, 3]]
a12 = [[3, 4], [5, 6]]

a21 = [[1], [2]]
a22 = [[3], [4]]

print(solution(a11, a12))
print(solution(a21, a22))
