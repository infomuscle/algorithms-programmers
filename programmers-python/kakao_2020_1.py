def solution(s):
    min_length = len(s)
    for i in range(1, len(s) + 1):
        ptr, cnt = 0, 1
        compressed = ""
        while ptr < len(s):
            if s[ptr:ptr + i] == s[ptr + i:ptr + i * 2]:
                cnt += 1
            else:
                if cnt > 1:
                    added = str(cnt) + s[ptr:ptr + i]
                else:
                    added = cnt * s[ptr:ptr + i]
                compressed += added
                cnt = 1
            ptr += i
        if len(compressed) < min_length:
            min_length = len(compressed)

    return min_length


s1 = "aabbaccc"
s2 = "ababcdcdababcdcd"
s3 = "abcabcdede"
s4 = "abcabcabcabcdededededede"
s5 = "xababcdcdababcdcd"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))
