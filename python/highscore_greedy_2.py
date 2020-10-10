def solution(number, k):
    target_length = len(number) - k
    stack = []

    for i in range(len(number)):
        # print(stack)
        if len(stack) + len(number) - i == target_length:
            stack.append(number[i])
        else:
            while len(stack) != 0 and stack[-1] < number[i] and len(stack) + len(number) - i != target_length:
                # if len(stack) != 0 and stack[-1] < number[i]:
                stack.pop()
            stack.append(number[i])
    # print(stack)

    answer = ""
    for i in range(target_length):
        answer += stack[i]

    return answer


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

print(solution(n1, k1))
print(solution(n2, k2))
print(solution(n3, k3))
print(solution(n4, k4))
print(solution(n5, k5))
