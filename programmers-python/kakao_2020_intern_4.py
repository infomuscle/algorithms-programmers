def solution(board):
    answer = 0
    n = len(board)
    graph = get_graph(board, n)

    stack = ["00"]
    while stack:
        cur = stack[-1]
        if cur in graph and len(graph[cur]) != 0:
            if graph[cur][-1] not in stack:
                stack.append(graph[cur].pop())
            else:
                graph[cur].pop()
                stack.pop()
        if stack[-1] == str(n - 1) + str(n - 1):
            break
    print(stack)

    straight, corner = 0, 0

    return answer


def get_graph(board, n):
    graph = {}
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                id = str(i) + str(j)
                tmp = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
                graph[id] = list()
                for t in tmp:
                    if t[0] < n and t[0] >= 0 and t[1] < n and t[1] >= 0 and board[t[0]][t[1]] == 0:
                        graph[id].append(str(t[0]) + str(t[1]))
                graph[id].sort()
    return graph


b1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b2 = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0]]
b3 = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
b4 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]

print(solution(b1))
print(solution(b2))
print(solution(b3))
print(solution(b4))
