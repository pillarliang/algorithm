#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

"""
When meet the boundary and the neighbor is water, the perimeter will increase by 1.
And these conditions just is the position of dfs() return.
"""
from typing import List


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        perimeter = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return self.dfs(r, c)

        return perimeter

    def dfs(self, row, col):
        if (
            row < 0
            or row >= len(self.grid)
            or col < 0
            or col >= len(self.grid[0])
            or self.grid[row][col] == 0
        ):

            return 1

        if self.visited[row][col]:  # !important code in this algorithm.
            return 0

        self.visited[row][col] = True
        perimeter = 0
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for r, c in direction:
            new_r = row + r
            new_c = col + c
            perimeter += self.dfs(new_r, new_c)

        return perimeter


# @lc code=end
