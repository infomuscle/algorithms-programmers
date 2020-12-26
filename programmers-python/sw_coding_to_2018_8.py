def solution(n):
    ans = 0

    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans


n1 = 5
n2 = 6
n3 = 5000
n4 = 1
n5 = 1000000000

print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
print(solution(n5))
