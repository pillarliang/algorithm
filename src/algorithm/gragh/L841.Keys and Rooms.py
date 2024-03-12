from typing import List
from queue import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = self.build_graph(rooms)
        visited = set()

        # DFS
        queue = deque([0])
        while len(queue) > 0:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        if len(graph) == len(visited):
            return True
        return False

    def canVisitAllRooms_dfs(self, rooms: List[List[int]]) -> bool:
        """BFS"""
        graph = self.build_graph(rooms)
        visited = set()
        self.BFS(graph, 0, visited)

        if len(graph) == len(visited):
            return True
        return False

    def BFS(self, graph, node, visited) -> bool:
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                self.BFS(graph, neighbor, visited)

    def build_graph(self, edges):
        graph = {}

        for index, edge in enumerate(edges):
            graph[index] = edge

        return graph
