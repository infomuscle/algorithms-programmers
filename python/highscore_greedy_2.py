def solution(number, k):
    max_num = number[:len(number) - k]

    for i in range(len(number) - k, len(number)):
        tmp = max_num + number[i]
        tmp_max = find_max(tmp)
        if tmp_max > int(max_num):
            max_num = str(tmp_max)

    answer = max_num
    return answer


def find_max(number):
    max_num = 0
    for i in range(len(number)):
        tmp = int(number[0:i] + number[i + 1:])
        if tmp > max_num:
            max_num = tmp

    return max_num


n1 = "1924"
k1 = 2
n2 = "1231234"
k2 = 3
n3 = "4177252841"
k3 = 4

print(solution(n1, k1))
print(solution(n2, k2))
print(solution(n3, k3))
