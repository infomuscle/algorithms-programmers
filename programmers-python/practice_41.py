def solution(land):
    land_length = len(land)

    for i in range(1, land_length):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[land_length - 1])


l1 = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
l2 = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1], [8, 9, 25, 12]]

print(solution(l1))
print(solution(l2))
