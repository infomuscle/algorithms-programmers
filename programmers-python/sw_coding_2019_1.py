def solution(w, h):
    answer = 0

    crossed = 0
    for i in range(w):
        for j in range(h):
            if (j + 1) / (i + 1) >= w / h and (j + 1) / (i + 1) <= h / w:
                print(i + 1, j + 1,  w, h)
                crossed += 1
    print(crossed)

    return answer


# w/h ~ h/w
# 2/3 ~ 3/2

# 1 1   -> 1
# 2 1   -> 1/2
# 2 2   -> 1
# 3 2   -> 2/3

# 4 3   -> 3/4
# 5 3   -> 3/5
# 5 4   -> 4/5
# 6 4   -> 2/3

# 7 5   -> 5/7
# 8 5   -> 5/8
# 8 6   -> 3/4
# 9 6   -> 2/3

# 10 7  -> 7/10
# 11 7  -> 7/11
# 11 8  -> 8/11
# 12 8  -> 2/3

w1, h1 = 8, 12  # 16 -> 2:3
w2, h2 = 8, 11  # 18 -> 8:11
w3, h3 = 8, 10  # 16 -> 4:5
w4, h4 = 8, 9   # 16 -> 8:9
w5, h5 = 8, 8  # 8   -> 1:1

print(solution(w1, h1))
print(solution(w2, h2))
