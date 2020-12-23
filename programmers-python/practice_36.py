def solution(s):
    stack = []
    for p in s:
        if len(stack) == 0 and p != "(":
            return False

        if p == "(":
            stack.append(p)
        else:
            if stack[-1] == "(":
                stack.pop()

    if len(stack) != 0:
        return False

    return True


s1 = "()()"
s2 = "(())()"
s3 = ")()("
s4 = "(()("

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
