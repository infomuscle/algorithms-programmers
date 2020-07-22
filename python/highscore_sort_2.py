def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    max = int(''.join(numbers))

    if len(numbers) == 1:
        return max

    # 하나씩 순서 바꿔보기 + 재귀
    i = 0
    start = 0
    while True:
        j = i + 1
        while True:
            # print(i, j, numbers)
            temp = swap(numbers, i, j)
            t = int(''.join(temp))
            if t > max:
                numbers = temp
                max = t
                i = 0
                j = i + 1
            else:
                j += 1
                if j == len(numbers):
                    break
        i += 1
        if i == len(numbers) - 1:
            break

    answer = str(max)

    return answer

def swap(numbers, i, j):
    swap = []
    swap += numbers
    swap[i], swap[j] = swap[j], swap[i]

    return swap


n1 = [6, 10, 2]
n2 = [3, 30, 34, 5, 9]
n3 = [0,0,0,1,0,3,0]
n4 = [1]

print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
