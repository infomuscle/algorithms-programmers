def solution(arr):
    arr = sorted(arr)

    num, adder = arr[-1], arr[-1]
    while True:
        is_lcm = True
        for a in arr:
            if num % a != 0:
                is_lcm = False
                break
        if is_lcm:
            break
        num += adder

    return num


a1 = [2, 6, 8, 14]
a2 = [1, 2, 3]
a3 = [1, 2, 3, 7, 17, 22, 23, 100]
a4 = [1, 2, 3, 4]

print(solution(a1))
print(solution(a2))
print(solution(a3))
print(solution(a4))
