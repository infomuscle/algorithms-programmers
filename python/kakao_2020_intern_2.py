from itertools import permutations


def solution(expression):
    answer = 0

    operators = ["+", "-", "*"]

    priorities = dict()
    for i, p in enumerate(permutations(operators, 3)):
        priorities[i] = list(p)
    print(priorities)

    expression_split = list()
    ptr = 0
    for i, e in enumerate(expression):
        if e in operators:
            expression_split.append(expression[ptr:i])
            expression_split.append(expression[i])
            ptr = i + 1
    expression_split.append(expression[ptr:])
    print(expression_split)
    print("-----------")

    for priority in priorities.values():
        postfix = []
        stack = []
        for e in expression_split:
            if e not in operators:
                postfix.append(e)
            else:
                while len(stack) != 0 and priority.index(stack[-1]) < priority.index(e):
                    postfix.append(stack.pop())
                stack.append(e)
        postfix.extend(stack)
        print(priority, postfix)

        stk = []
        for p in postfix:
            if p not in operators:
                stk.append(p)
            else:
                stk.append(calculator(p, int(stk.pop()), int(stk.pop())))

        reward = stk.pop()
        if abs(reward) > answer:
            answer = abs(reward)

    return answer


def calculator(op: str, num1: int, num2: int):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    else:
        result = num1 * num2

    return result


e1 = "100-200*300-500+20"
e2 = "50*6-3*2"

print(solution(e1))
print("###########")
print(solution(e2))
