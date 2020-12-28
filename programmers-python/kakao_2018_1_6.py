import re


def solution(str1, str2):
    jaccard = 65536

    l1, l2 = [], []
    for i in range(len(str1) - 1):
        s1 = str1[i:i + 2].upper()
        if re.match(r'^[a-zA-Z]*$', s1):
            l1.append(s1)
    for i in range(len(str2) - 1):
        s2 = str2[i:i + 2].upper()
        if re.match(r'^[a-zA-Z]*$', s2):
            l2.append(s2)

    if len(l1) == 0 and len(l2) == 0:
        jaccard *= 1
    else:
        jaccard *= (len(get_intersection(l1, l2)) / len(get_union(l1, l2)))

    return int(jaccard)


def get_intersection(list1, list2):
    intersection = []

    for l in set(list1):
        tmp = [l] * min(list1.count(l), list2.count(l))
        intersection.extend(tmp)

    return intersection


def get_union(list1, list2):
    union = []

    for l in set(list1 + list2):
        tmp = [l] * max(list1.count(l), list2.count(l))
        union.extend(tmp)

    return union


s11, s12 = "FRANCE", "french"
s21, s22 = "handshake", "shake hands"
s31, s32 = "aa1+aa2", "AAAA12"
s41, s42 = "E=M*C^2", "e=m*c^2"

print(solution(s11, s12))
print(solution(s21, s22))
print(solution(s31, s32))
print(solution(s41, s42))
