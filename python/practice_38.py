def solution(n):
    answer = ''

    map = {"1": "1", "2": "2", "3": "4", }

    bound = 0
    square = 1
    while True:
        bound += 3 ** square
        if bound >= n:
            break
        square += 1

    tmp = ""
    while True:
        square -= 1
        a = str(n // 3 ** square)
        if a != "0":
            tmp += a
        else:
            tmp = tmp[:len(tmp) - 1] + str(int(tmp[-1]) - 1) + "3"
        n = n % 3 * square
        if square == 0:
            break

    for t in tmp:
        answer += map[t]

    return answer


n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n6 = 6
n7 = 7
n8 = 8

print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
print(solution(n5))
print(solution(n6))
print(solution(n7))
print(solution(n8))

# 1 = A 3^0 * 1
# 2 = B 3^0 * 2
# 3 = C 3^0 * 3
#
# 4 = AA 3^1 * 1 + 3^0*1
# 5 = AB
# 6 = AC
# 7 = BA
# 8 = BB
# 9 = BC
# 10 = CA
# 11 = CB
# 12 = CC 3^1 * 3 + 3^0 * 3

#
# 13 = AAA
