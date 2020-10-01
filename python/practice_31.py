def solution(n):
    answer = 0

    primes = [2]

    for i in range(3, n + 1, 2):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    answer = len(primes)

    return answer


n1 = 10
n2 = 5
n3 = 1000000

print(solution(n1))
print(solution(n2))
print(solution(n3))
