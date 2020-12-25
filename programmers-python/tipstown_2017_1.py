def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0 or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()

    if len(stack) == 0:
        return 1

    return 0


s1 = "baabaa"
s2 = "cdcd"
s3 = "a" * 1000000

print(solution(s1))
print(solution(s2))
print(solution(s3))
