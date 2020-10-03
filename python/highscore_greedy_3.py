def solution(name):
    answer = 0

    current = "A" * len(name)
    idx = 0
    while True:
        button = ord(name[idx]) - ord('A')
        if button > 13:
            button = 26 - button
        answer += button
        current = current[:idx] + name[idx] + current[idx + 1:]

        if current == name:
            break

        if current[idx + 1] != name[idx + 1]:
            idx += 1
            answer += 1
        else:
            idx -= 1
            answer += 1

        if idx < 0:
            idx = len(name) + idx
        elif idx >= len(name):
            idx = 0

    return answer


n1 = "JEROEN"
n2 = "JAN"
n3 = "ADFECBFAERFADFAS"

# print(solution(n1))
# print(solution(n2))
print(solution(n3))
