def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = reversed(quick_sort(numbers))

    answer = ''.join(numbers)
    return answer


def quick_sort(numbers):
    if len(numbers) < 2:
        return numbers

    pivot = numbers[0]
    forward, backward = [], []
    for i in range(1, len(numbers)):
        if int(pivot + numbers[i]) < int(numbers[i] + pivot):
            backward.append(numbers[i])
        else:
            forward.append(numbers[i])

    return quick_sort(forward) + [pivot] + quick_sort(backward)


n1 = [6, 10, 2]
n2 = [3, 30, 34, 5, 9]
n3 = [0, 0, 0, 1, 0, 3, 0]
n4 = [9]

print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
