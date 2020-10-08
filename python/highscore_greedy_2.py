def solution(number, k):
    # 제일 큰 앞자리 수 찾기
    idx = 0
    first_no = "0"
    first_idx = 0
    while idx < k:
        if number[idx] > first_no:
            first_no = number[idx]
            first_idx = idx
        idx += 1
    number = number[first_idx:]
    k -= first_idx

    # 남은 거 제거하기
    idx = 0
    remove_cnt = 0
    tmp = ""
    for i in range(len(number) - 1):
        if number[idx] < number[idx + 1]:
            remove_cnt += 1
        else:
            tmp += number[idx]
        idx += 1
        if remove_cnt >= k:
            break
    number = tmp + number[idx:]
    k -= remove_cnt

    if k > 0:
        for i in range(k):
            for j in range(10):
                if str(j) in number:
                    number = number.replace(str(j), "", 1)
                    break

    return number


n1 = "1924"
k1 = 2
n2 = "1231234"
k2 = 3
n3 = "4177252841"
k3 = 4
n4 = "1234567890"
k4 = 6
n5 = "987654321"
k5 = 4

# print(solution(n1, k1))
# print(solution(n2, k2))
# print(solution(n3, k3))
# print(solution(n4, k4))
print(solution(n5, k5))
