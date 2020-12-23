def solution(dartResult):
    multiplier = ["S", "D", "T"]
    option = ["*", "#"]

    stack = []

    for i, d in enumerate(dartResult):
        if d.isdigit():
            if d == "1" and dartResult[i + 1] == "0":
                stack.append(10)
            elif d == "0" and dartResult[i - 1] == "1":
                pass
            else:
                stack.append(int(d))
        elif d in multiplier:
            if d == "D":
                squarer = 2
            elif d == "T":
                squarer = 3
            else:
                squarer = 1
            stack.append(stack.pop() ** squarer)
        elif d in option:
            top = stack.pop()
            if d == "*":
                if len(stack) != 0:
                    stack.append(stack.pop() * 2)
                top *= 2
            elif d == "#":
                top = -top
            stack.append(top)

    return sum(stack)


d1 = "1S2D*3T"
d2 = "1D2S#10S"
d3 = "1D2S0T"
d4 = "1S*2T*3S"
d5 = "1D#2S*3S"
d6 = "1T2D3D#"
d7 = "1D2S3T*"

print(solution(d1))
print(solution(d2))
print(solution(d3))
print(solution(d4))
print(solution(d5))
print(solution(d6))
print(solution(d7))
