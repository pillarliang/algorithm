from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    self.dfs(r, c)

    def dfs(self, row, col):
        if (
            row < 0
            or row >= len(self.grid)
            or col < 0
            or col >= len(self.grid)
            or self.visited[row][col]
            or self.grid[row][col] == 0
        ):

            return
        self.visited[row][col] = True
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for r, c in direction:
            new_r = row + r
            new_c = col + c
            self.dfs(new_r, new_c)
