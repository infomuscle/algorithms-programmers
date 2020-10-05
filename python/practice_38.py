def solution(n):
    answer = ""

    map1 = {1: "A", 2: "B", 0: "C"}
    map2 = {"A": 1, "B": 2, "C": 3}
    map3 = {1: "A", 2: "B", 3: "C"}

    chrs = ""
    remains = n % 3
    chr = str(map1[remains])
    chrs += chr
    n -= map2[chr]

    square = 1
    while True:
        if n == 0:
            break
        for i in range(3, 0, -1):
            if n == ((3 ** square) * i):
                chrs += map3[i]
                n -= (3 ** square) * i
                break
        square += 1
    answer = chrs[::-1]
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
print(solution(n13))
