def solution(n, computers):
    networks = {}
    for i, computer in enumerate(computers):
        connected = []
        for j, c in enumerate(computer):
            if c == 1:
                connected.append(j)
        networks[i] = set(connected)

    connection = []
    for network in networks:
        visited = []
        stack = [network]
        while stack:
            node = stack.pop()
            visited.append(node)
            visitable = networks[node]
            stack.extend(list(set(visitable) - set(visited)))
        if set(visited) not in connection:
            connection.append(set(visited))

    return len(connection)


n1 = 3
c1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n2 = 3
c2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n1, c1))
print(solution(n2, c2))
