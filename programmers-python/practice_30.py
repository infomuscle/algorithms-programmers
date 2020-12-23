def solution(n, m):
    answer = []

    if n <= m:
        endpoint = n
    else:
        endpoint = m

    common_divisiors = []
    common_multiples = []
    for i in range(1, endpoint + 1):
        if n % i == 0 and m % i == 0:
            common_divisiors.append(i)

    offset = 0
    while True:
        num = endpoint + offset
        if num % n == 0 and num % m == 0:
            common_multiples.append(num)
            break
        offset += 1

    answer.append(common_divisiors[-1])
    answer.append(common_multiples[0])

    return answer


n1 = 3
m1 = 12
n2 = 2
m2 = 5

print(solution(n1, m1))
print(solution(n2, m2))
