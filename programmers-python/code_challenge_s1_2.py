def solution(n):
    snail = []
    for i in range(n):
        tmp = [0] * (i + 1)
        tmp.append(-1)
        snail.append(tmp)
    snail.append([-1] * (n + 1))

    cells = n * (n + 1) // 2
    i, j, num = 0, 0, 0
    way = "down"
    while num < cells:
        num += 1
        snail[i][j] = num
        way = check_way(snail, i, j, way)
        if way == "down":
            i += 1
        elif way == "right":
            j += 1
        elif way == "up":
            i -= 1
            j -= 1

    answer = []
    for floor in snail:
        for cell in floor:
            if cell != -1:
                answer.append(cell)

    return answer


def check_way(snail, i, j, way):
    if snail[i + 1][j] != 0 and snail[i][j + 1] == 0 and way == "down":
        way = "right"
    elif snail[i][j + 1] != 0 and snail[i + 1][j] != 0 and snail[i - 1][j - 1] == 0 and way == "right":
        way = "up"
    elif snail[i - 1][j - 1] != 0 and snail[i + 1][j] == 0 and way == "up":
        way = "down"

    return way


n1 = 4
n2 = 5
n3 = 6

print(solution(n1))
print(solution(n2))
print(solution(n3))

#              00
#            10 11
#          20 21 22
#        30 31 32 33
#      40 41 42 43 44
#    50 51 52 53 54 55


# 00 50 55
# 11 42 43
# 32
