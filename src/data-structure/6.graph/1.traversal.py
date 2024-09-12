from collections import deque


class UndirectedGraph(object):
    def __init__(self, vertex_num: int) -> None:
        self._vertex_num = vertex_num
        self._adjacency = [[] for _ in range(vertex_num)]

    def add_edge(self, s: int, t: int):
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def bfs(self, start):
        """广度优先"""
        visited = set()
        queue = deque([start])

        while len(queue) > 0:
            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self._adjacency[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        print(visited)

    def dfs(self, node, visited):
        """深度优先"""
        if node in visited:
            return

        visited.append(node)

        for neighbor in self._adjacency[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


graph = UndirectedGraph(8)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 7)
graph.add_edge(6, 7)
graph.bfs(0)
graph.dfs(0, [])
