def solution(board):
    row_size = len(board)
    col_size = len(board[0])

    side_size = min(row_size, col_size)
    while side_size > 0:
        max_found = False
        for i in range(row_size - side_size + 1):
            for j in range(col_size - side_size + 1):
                if check_square(board, i, j, side_size):
                    max_found = True
                    break
            if max_found:
                break
        if max_found:
            break
        side_size -= 1

    return side_size ** 2


def check_square(board, x, y, n):
    valid = True
    try:
        for i in range(n):
            for j in range(n):
                if board[x + i][y + j] == 0:
                    valid = False
                    break
    except:
        valid = False

    return valid


b1 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
b2 = [[0, 0, 1, 1], [1, 1, 1, 1]]

print(solution(b1))
print(solution(b2))
