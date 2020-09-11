class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.children = [None, None]

    def left_child(self, node):
        self.children[0] = node
        return self

    def right_child(self, node):
        self.children[1] = node
        return self


def solution(numbers, target):
    answer = 0
    tree = get_tree(numbers)

    return answer


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


def get_tree(numbers):
    tree = {}

    node = Node(0, numbers[0])
    node.left_child(Node(1, numbers[1]))
    node.right_child(Node(1, -numbers[1]))
    tree[node] = {node.children[0], node.children[1]}

    for i in range(1, len(numbers) - 1):
        node1 = Node(i, numbers[i])
        node1.left_child(Node(i + 1, numbers[i + 1]))
        node1.right_child(Node(i + 1, -numbers[i + 1]))
        tree[node1] = {node1.children[0], node1.children[1]}

        node2 = Node(i, -numbers[i])
        node2.left_child(Node(i + 1, numbers[i + 1]))
        node2.right_child(Node(i + 1, -numbers[i + 1]))
        tree[node2] = {node2.children[0], node2.children[1]}

    for t in tree:
        print(str(t.index) + ":" + str(t.value) + ":" + str(t.children[0].value) + ":" + str(t.children[1].value))

    return tree


n1 = [1, 1, 1, 1, 1]
n2 = [1, 2, 3, 4, 5]

print(get_tree(n2))
