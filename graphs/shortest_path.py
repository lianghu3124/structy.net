'''
https://structy.net/problems/shortest-path
https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=5043s
'''

from collections import deque
from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    return graph


def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)

    visited = set(node_A)
    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == node_B:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance+1))

    return -1


if __name__ == '__main__':

    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    assert shortest_path(edges, 'w', 'z') == 2

    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    assert shortest_path(edges, 'y', 'x') == 1

    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]
    assert shortest_path(edges, 'a', 'e') == 3

    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]
    assert shortest_path(edges, 'e', 'c') == 2

    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]
    assert shortest_path(edges, 'b', 'g') == -1

    edges = [
        ['c', 'n'],
        ['c', 'e'],
        ['c', 's'],
        ['c', 'w'],
        ['w', 'e'],
    ]
    assert shortest_path(edges, 'w', 'e') == 1

    edges = [
        ['c', 'n'],
        ['c', 'e'],
        ['c', 's'],
        ['c', 'w'],
        ['w', 'e'],
    ]
    assert shortest_path(edges, 'n', 'e') == 2

    edges = [
        ['m', 'n'],
        ['n', 'o'],
        ['o', 'p'],
        ['p', 'q'],
        ['t', 'o'],
        ['r', 'q'],
        ['r', 's']
    ]
    assert shortest_path(edges, 'm', 's') == 6

    print('OK')