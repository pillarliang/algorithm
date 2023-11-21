def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        size = get_size(graph, node, visited)
        if size > largest:
            largest = size

    return largest


def get_size(graph, current, visited):
    if current in visited:
        return 0

    visited.add(current)
    size = 1

    for neighbor in graph[current]:
        size += get_size(graph, neighbor, visited)

    return size
