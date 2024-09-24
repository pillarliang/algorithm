#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
from collections import deque

"""
Iterately traverse the grid, if meet a "1" and not visited, then start a bfs to mark all the connected "1" as visited, and counter +1.

For BFS: 只要 加入队列就代表 走过，就需要标记，而不是从队列拿出来的时候再去标记走过。
"""


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid

        n, m = len(grid), len(grid[0])
        self.visited = [[False] * m for _ in range(n)]
        island = 0

        for i in range(n):
            for j in range(m):
                if self.grid[i][j] == "1" and not self.visited[i][j]:
                    island += 1
                    self.bfs(i, j)

        return island

    def bfs(self, row, col):
        queue = deque([(row, col)])
        self.visited[row][col] = True
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while queue:
            cur_x, cur_y = queue.popleft()
            for x, y in directions:
                next_x = cur_x + x  # row
                next_y = cur_y + y  # col

                if (
                    0 <= next_x < len(self.grid)
                    and 0 <= next_y < len(self.grid[0])
                    and not self.visited[next_x][next_y]
                    and self.grid[next_x][next_y] == "1"
                ):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y))


# @lc code=end
