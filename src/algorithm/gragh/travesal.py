from collections import deque


def depthFirst(graph, source):
    queue = [source]
    while len(queue) > 0:
        cur = queue.pop()
        print(cur)
        for item in graph.get(cur):
            queue.append(item)


def depthFist2(graph, source):
    print(source)
    for node in graph.get(source):
        depthFist2(graph, node)


def bfs(graph, source):
    queue = deque([source])
    res = []
    while len(queue) > 0:
        node = queue.popleft()
        res.append(node)
        print(node)
        for item in graph.get(node):
            if item not in res:
                queue.append(item)


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

bfs(graph, 'a')  # adbfce
