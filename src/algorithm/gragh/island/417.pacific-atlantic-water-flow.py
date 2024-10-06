#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # 初始化两个可达性矩阵
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]

        # 定义深度优先搜索方式
        def dfs(r, c, reachable):
            reachable[r][c] = True
            # 四个方向移动
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 检查边界和高度的条件
                if 0 <= nr < m and 0 <= nc < n and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)

        # 从接触太平洋的边界开始DFS
        for i in range(m):
            dfs(i, 0, pacific_reachable)  # 左边界
            dfs(i, n - 1, atlantic_reachable)  # 右边界

        for j in range(n):
            dfs(0, j, pacific_reachable)  # 上边界
            dfs(m - 1, j, atlantic_reachable)  # 下边界

        # 合并结果
        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result

# @lc code=end

