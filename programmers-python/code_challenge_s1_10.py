def solution(s):
    cnt, zeros = 0, 0
    while s != "1":
        converted = convert(s)
        s = converted[0]
        zeros += converted[1]
        cnt += 1

    return [cnt, zeros]


def convert(string):
    zeros = string.count("0")
    removed = string.replace("0", "")
    return [format(len(removed), 'b'), zeros]


s1 = "110010101001"
s2 = "01110"
s3 = "1111111"

print(solution(s1))
print(solution(s2))
print(solution(s3))
