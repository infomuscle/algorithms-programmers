def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr = []
        for k in range(len(arr2[0])):
            sum = 0
            for j in range(len(arr1[i])):
                sum += arr1[i][j] * arr2[j][k]
            arr.append(sum)
        answer.append(arr)

    return answer


a11 = [[1, 4], [3, 2], [4, 1]]
a21 = [[3, 3], [3, 3]]
a12 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
a22 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(a11, a21))
print(solution(a12, a22))

# 00 01 02      00 01
# 10 11 12      10 11
# 20 21 22      20 21


# 1 4       3 3     3+12  3+12      15 15
# 3 2       3 3     9+6   9+6       15 15
# 4 1                               15 15
