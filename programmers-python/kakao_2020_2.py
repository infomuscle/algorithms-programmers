def solution(p):
    return resolver(p)


def resolver(bracket):
    if len(bracket) == 0:
        return ""

    len_open, len_close = 0, 0
    for b in bracket:
        if b == "(":
            len_open += 1
        else:
            len_close += 1
        if len_open == len_close:
            break

    u, v = bracket[:len_open + len_close], bracket[len_open + len_close:]
    op = {"(": ")", ")": "("}

    if bracket_checker(u):
        u += resolver(v)
    else:
        resolved = "(" + resolver(v) + ")"
        u = u[1:-1]
        for p in u:
            resolved += op[p]
        return resolved

    return u


def bracket_checker(bracket):
    stack = []

    for b in bracket:
        if b == "(":
            stack.append(b)
            continue
        if len(stack) == 0 or stack[-1] != "(":
            return False
        else:
            stack.pop()

    if len(stack) != 0:
        return False

    return True


p1 = "(()())()"
p2 = ")("
p3 = "()))((()"
p4 = ""
print(solution(p1))
print(solution(p2))
print(solution(p3))
print(solution(p4))
