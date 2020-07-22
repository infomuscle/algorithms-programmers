def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))

    max = ''.join(numbers)

    # 하나씩 순서 바꿔보기 + 재귀
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp = swap(numbers, i, j)
            # print(temp, numbers)
            if int(''.join(temp)) > int(max):
                numbers = temp
                max = ''.join(numbers)

    answer = max

    return answer

def swap(numbers, i, j):
    swap = []
    swap += numbers
    temp = swap[j]
    swap[j] = swap[i]
    swap[i] = temp

    return swap


n1 = [6, 10, 2]
n2 = [3, 30, 34, 5, 9]

print(solution(n1))
print(solution(n2))
