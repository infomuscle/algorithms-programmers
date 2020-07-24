def solution(strings, n):
    answer = quick_sort(strings, n)
    return answer


def quick_sort(strings, n):
    if len(strings) < 2:
        return strings

    pivot = strings[0]
    forward, backward = [], []
    for i in range(1, len(strings)):
        if ord(strings[i][n]) < ord(pivot[n]):
            forward.append(strings[i])
        elif ord(strings[i][n]) > ord(pivot[n]):
            backward.append(strings[i])
        else:
            if strings[i] < pivot:
                forward.append(strings[i])
            else:
                backward.append(strings[i])

    return quick_sort(forward, n) + [pivot] + quick_sort(backward, n)


s1 = ["sun", "bed", "car"]
n1 = 1
s2 = ["abce", "abcd", "cdx"]
n2 = 2

print(solution(s1, n1))
print(solution(s2, n2))
print("abcd" < "abce")
