def solution(blocks):
    answer = []

    block_map = dict()
    for i, block in enumerate(blocks):
        if i not in block_map.keys():
            block_map[i] = dict()
        block_map[i][block[0]] = block[1]
    print(block_map)

    for row in block_map.keys():
        print(row)
        for col in block_map[row].keys():
            try:
                left = block_map[row + 1][col]
            except:
                block_map[row + 1][col] = block_map[row][col] - block_map[row + 1][col + 1]
            try:
                right = block_map[row + 1][col + 1]
            except:
                block_map[row + 1][col + 1] = block_map[row][col] - block_map[row + 1][col]
        print(block_map)

    return answer


b1 = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
b2 = [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]

print(solution(b1))
print(solution(b2))
