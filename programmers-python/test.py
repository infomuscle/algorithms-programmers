from collections import deque

graph = {
    'A': {'B'},
    'B': {'A', 'C', 'H'},
    'C': {'B', 'D'},
    'D': {'C', 'E', 'G'},
    'E': {'D', 'F'},
    'F': {'E'},
    'G': {'D'},
    'H': {'B', 'I', 'J', 'M'},
    'I': {'H'},
    'J': {'H', 'K'},
    'K': {'J', 'L'},
    'L': {'K'},
    'M': {'H'}
}


def bfs(graph, start_node):
    visited = list()
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        print(node)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node] - set(visited))

    return visited


def dfs(graph, start_node):
    visited = list()
    stack = list()
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node] - set(visited))

    return visited


print(bfs(graph, 'A'))
