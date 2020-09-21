import heapq
from itertools import permutations


def solution(expression):
    answer = 0

    operators = ["+", "-", "*"]

    priorities = dict()
    for i, p in enumerate(permutations(operators, 3)):
        priorities[i] = list(p)
    print(priorities)

    nums, ops = dict(), dict()
    ptr, idx = 0, 0
    for i, e in enumerate(expression):
        if e in operators:
            nums[idx] = expression[ptr:i]
            ops[idx] = expression[i]
            idx += 1
            ptr = i + 1
    nums[idx] = expression[ptr:]
    print(nums, ops)

    for priority in priorities.values():
        ops_heap = list()
        for op in ops.keys():
            # print(ops[op], priority.index(ops[op]))
            heapq.heappush(ops_heap, (priority.index(ops[op]), op))
        print(ops_heap)

    return answer


def calculator(op, num1, num2):
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
print(solution(e2))
