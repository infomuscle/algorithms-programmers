from collections import deque


def solution(blocks):
    answer = []

    block_map = dict()
    for i, block in enumerate(blocks):
        if i not in block_map.keys():
            block_map[i] = dict()
        block_map[i][block[0]] = block[1]

    last_row = sorted(block_map.keys())[-1]
    answer.append(block_map[0][0])
    for i, row in enumerate(block_map.keys()):
        if i == last_row:
            break

        block_on_row = deque(block_map[row].items())
        while len(block_map[row]) < row + 1 or len(block_map[row + 1].keys()) < row + 1 + 1:
            block = block_on_row.popleft()
            if block[0] not in block_map[row + 1].keys() and block[0] + 1 in block_map[row + 1].keys():
                block_map[row + 1][block[0]] = block_map[row][block[0]] - block_map[row + 1][block[0] + 1]
            elif block[0] in block_map[row + 1].keys() and block[0] + 1 not in block_map[row + 1].keys():
                block_map[row + 1][block[0] + 1] = block_map[row][block[0]] - block_map[row + 1][block[0]]
            else:
                block_on_row.append(block)

        for b in sorted(block_map[row + 1].keys()):
            answer.append(block_map[row + 1][b])

    return answer


b1 = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
b2 = [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]

print(solution(b1))
print(solution(b2))
