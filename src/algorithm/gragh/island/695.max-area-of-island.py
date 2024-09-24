#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
from typing import List


# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        max_island_num = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == 1:
                    count = self.dfs(row, col)
                    max_island_num = max(count, max_island_num)

        return max_island_num

    def dfs(self, row, col):
        if (
            row < 0
            or row >= len(self.grid)
            or col < 0
            or col >= len(self.grid[0])
            or self.visited[row][col]
            or self.grid[row][col] == 0
        ):
            return 0

        self.visited[row][col] = True
        count = 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r, c in directions:
            count += self.dfs(row + r, col + c)
        return count


# @lc code=end

# Test the code with the provided test case
grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]

solution = Solution()
print(solution.maxAreaOfIsland(grid))  # Expected output: 6
