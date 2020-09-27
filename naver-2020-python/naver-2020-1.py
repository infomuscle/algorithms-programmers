from collections import deque


def solution(m, k):
    key_queue = deque(k)

    k_index = []
    idx = 0
    while len(key_queue) != 0:
        key = key_queue.popleft()
        for i, m_chr in enumerate(m):
            if m_chr == key and i >= idx:
                k_index.append(i)
                idx = i
                break

    encrypted = ""
    for i, m_chr in enumerate(m):
        if i not in k_index:
            encrypted += m_chr

    return encrypted


m1 = "kkaxbycyz"
k1 = "abc"
m2 = "acbbcdc"
k2 = "abc"

print(solution(m1, k1))
print(solution(m2, k2))
