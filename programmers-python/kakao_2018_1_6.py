import re


def solution(str1, str2):
    regex = re.compile(r'^[a-zA-Z]*$')
    l1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if re.match(regex, str1[i:i + 2].upper())]
    l2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if re.match(regex, str2[i:i + 2].upper())]

    if len(l1) == 0 and len(l2) == 0:
        jaccard = 1
    else:
        jaccard = len(get_intersection(l1, l2)) / len(get_union(l1, l2))

    return int(jaccard * 65536)


def get_intersection(list1, list2):
    intersection = []

    for l in set(list1):
        intersection.extend([l] * min(list1.count(l), list2.count(l)))

    return intersection


def get_union(list1, list2):
    union = []

    for l in set(list1 + list2):
        union.extend([l] * max(list1.count(l), list2.count(l)))

    return union


s11, s12 = "FRANCE", "french"
s21, s22 = "handshake", "shake hands"
s31, s32 = "aa1+aa2", "AAAA12"
s41, s42 = "E=M*C^2", "e=m*c^2"

print(solution(s11, s12))
print(solution(s21, s22))
print(solution(s31, s32))
print(solution(s41, s42))
