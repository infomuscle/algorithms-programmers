def solution(key, lock):
    answer = True

    print(rotation(key))

    return answer


def rotation(arr):
    """
    2차원 배열을 시계 방향으로 90도 회전
    """
    length = len(arr)
    rot = []
    for i in range(length):
        row = []
        for j in range(length):
            print(length - 1 - j, i)
            row.append(arr[length - 1 - j][i])
        rot.append(row)

    return rot


def check(arr):
    for row in arr:
        for col in row:
            if col != 1:
                return False

    return True


k1 = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]

k1r = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]]

l1 = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]

print(solution(k1, l1))
