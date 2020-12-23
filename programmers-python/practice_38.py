def solution(n):
    answer = ""

    square = 1
    while n > 0:
        divider = 3 ** square
        remain = n % divider
        d = 3 ** (square - 1)
        # print(n, divider, remain)
        if remain // d == 1:
            answer += "1"
        elif remain // d == 2:
            answer += "2"
        elif remain // d == 0:
            answer += "4"
            remain = (3 ** (square - 1)) * 3
        n -= remain
        square += 1

    answer = answer[::-1]
    return answer


n1 = 1  # A 3^0*A
n2 = 2  # B 3^0*B
n3 = 3  # C 3*0*C

n4 = 4  # AA 3^1*A + 3^0*A
n5 = 5  # AB 3^1*A + 3^0*B
n6 = 6  # AC 3^1*A + 3^0*C

n7 = 7  # BA 3^1*B + 3^0*A
n8 = 8  # BB 3^1*B + 3^0*B
n9 = 9  # BC 3^1*B + 3^0*C

n10 = 10  # CA 3^1*C + 3^0*A
n11 = 11  # CB 3^1*C + 3^0*B
n12 = 12  # CC 3^1*C + 3^0*C

n13 = 13  # AAA 3^2*A + 3^1*A + 3^0*A

# print(solution(n1))
# print(solution(n2))
# print(solution(n3))
# print(solution(n4))
# print(solution(n5))
# print(solution(n6))
# print(solution(n7))
# print(solution(n8))
# print(solution(n9))
# print(solution(n10))
# print(solution(n11))
# print(solution(n12))
# print(solution(n13))

for i in range(100):
    print(i + 1, solution(i + 1))
