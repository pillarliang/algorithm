from collections import deque


def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()

        if node == node_B:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, distance+1))
                visited.add(neighbor)

    return -1


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z'))  # -> 2
