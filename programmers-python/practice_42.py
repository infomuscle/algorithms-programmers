def solution(board):
    row_size, col_size = len(board), len(board[0])
    for i in range(1, row_size):
        for j in range(1, col_size):
            if board[i][j] > 0:
                one, two, three = board[i - 1][j], board[i - 1][j - 1], board[i][j - 1]
                if one > 0 and two > 0 and three > 0:
                    board[i][j] = min(one, two, three) + 1
    max_in_rows = [max(row) for row in board]

    return max(max_in_rows) ** 2


b1 = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 0]
]
b2 = [[0, 0, 1, 1], [1, 1, 1, 1]]

print(solution(b1))
print(solution(b2))
