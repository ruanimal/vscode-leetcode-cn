"""深度优先搜索
"""

import pprint
from collections import namedtuple, deque

Pos = namedtuple('Pos', ['x', 'y'])


def dfs(graph, node):
    visited = set()
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            process(node)
            nodes = generate_related_nodes(graph, node)
            stack.extend(nodes[::-1])

def generate_related_nodes(graph, node):
    max_x = len(graph) - 1
    max_y = len(graph[0]) - 1
    res = []
    for x, y in [
        (node.x-1, node.y),
        (node.x, node.y+1),
        (node.x+1, node.y),
        (node.x, node.y-1),
    ]:
        if 0 <= x <= max_x and 0 <= y <= max_y:
            res.append(Pos(x, y))
    return res

def process(node: Pos):
    print(graph[node.x][node.y])


graph = [list(range(i, i+5)) for i in range(0, 25, 5)]
pprint.pprint(graph)

# bfs(graph, Pos(0, 0))
dfs(graph, Pos(0, 0))
