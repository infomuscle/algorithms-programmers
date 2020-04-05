def solution(inputString):
    answer = -1
    stack = []
    openings = ["(", "{", "[", "<"]
    closings = [")", "}", "]", ">"]
    temp = []
    count = 0

    for s in inputString:
        if s in openings:
            stack.append(s)

        if s in closings:
            while len(stack) != 0:
                b = stack.pop()
                if openings.index(b) == closings.index(s):
                    count += 1
                    temp.reverse()
                    for t in temp:
                        stack.append(t)
                    temp = []
                    break
                else:
                    temp.append(b)
            if len(temp) != 0:
                temp.reverse()
                for t in temp:
                    stack.append(t)
                temp = []

    if len(stack) == 0:
        answer = count

    return answer

tc1 = "Hello, world!"
tc2 = "line [plus]"
tc3 = "if (Count of eggs is 4.) {Buy milk.}"
tc4 = ">_<"
tc5 = "([)]"
tc6 = ")("
tc7 = "[[[))]"
tc8 = "<>{}[][<<>]>"

print(solution(tc1))
print(solution(tc2))
print(solution(tc3))
print(solution(tc4))
print(solution(tc5))
print(solution(tc6))
print(solution(tc7))
print(solution(tc8))
