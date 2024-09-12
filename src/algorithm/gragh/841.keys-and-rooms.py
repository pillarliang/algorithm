#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
from typing import List
from collections import deque

# @lc code=start
class Solution_DFS:
    """
    本题的特性是 根据 visited 的长度返回True or False。
    """
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = self.build_graph(rooms)
        visited = set()
        self.DFS(graph, 0, visited)
        if len(rooms) == len(visited):
            return True
        return False
        
    def build_graph(self, rooms):
        graph = {}
        for index, item in enumerate(rooms):
            if index not in graph:
                graph[index] = []
            graph[index].extend(item)
            
        return graph
    
    def DFS(self, graph, node, visited):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph[node]:
            self.DFS(graph, neighbor, visited)
            
class Solution:
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = self.build_graph(rooms)
        visited = set()
        
        queue = deque([0])
        
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            
            visited.add(node)
            
            for neignbor in graph[node]:
                if neignbor not in visited:
                    queue.append(neignbor)
        if len(rooms) == len(visited):
            return True
        return False
            
        
    def build_graph(self, rooms):
        graph = {}
        for index, item in enumerate(rooms):
            if index not in graph:
                graph[index] = []
            graph[index].extend(item)
            
        return graph
    
            
        
# @lc code=end
rooms = [[1,3],[3,0,1],[2],[0]] # false
print(Solution().canVisitAllRooms(rooms))

# rooms = [[1],[2],[3],[]]
# print(Solution().canVisitAllRooms(rooms)) # true