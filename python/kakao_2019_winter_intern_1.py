def solution(board, moves):
    answer = 0
    stk = []
    newBoard = []

    for i in range(len(board)):
        temp = []
        for j in range(len(board[i])-1, -1, -1):
            if board[j][i] != 0:
                temp.append(board[j][i])
        newBoard.append(temp)

    for m in moves:
        if len(newBoard[m-1]) != 0:
            x = newBoard[m-1].pop()
            if len(stk) == 0 or stk[len(stk)-1] != x:
                stk.append(x)
            elif stk[len(stk)-1] == x:
                stk.pop()
                answer += 2

    return answer


b1 = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m1 = [1,5,3,5,1,2,1,4]

print(solution(b1, m1))
