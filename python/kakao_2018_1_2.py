def solution(n, arr1, arr2):
    map1, map2 = [], []
    for i in range(n):
        map1.append(str(bin(arr1[i]))[2:].zfill(n))
        map2.append(str(bin(arr2[i]))[2:].zfill(n))

    treasure_map = []
    for i in range(n):
        line = ""
        for j in range(n):
            line += "#" if map1[i][j] == "1" or map2[i][j] == "1" else " "
        treasure_map.append(line)

    return treasure_map


n1 = 5
a11 = [9, 20, 28, 18, 11]
a21 = [30, 1, 21, 17, 28]

n2 = 6
a12 = [46, 33, 33, 22, 31, 50]
a22 = [27, 56, 19, 14, 14, 10]

print(solution(n1, a11, a21))
print(solution(n2, a12, a22))
