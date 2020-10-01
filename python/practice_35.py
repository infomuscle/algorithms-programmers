def solution(n):
    cnt_of_1 = str(bin(n)).count("1")
    num = n + 1
    while True:
        if str(bin(num)).count("1") == cnt_of_1:
            break
        num += 1

    return num


n1 = 78
n2 = 15

print(solution(n1))
print(solution(n2))
