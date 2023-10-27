#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import List


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        table = [float('inf')] * (len(cost))
        table[0] = cost[0]
        table[1] = cost[1]

        for index, item in enumerate(table):
            if index + 1 < len(cost):
                table[index + 1] = min(item + cost[index + 1],
                                       table[index + 1])
            if index + 2 < len(cost):
                table[index + 2] = min(item + cost[index + 2],
                                       table[index + 2])

        return min(table[-1], table[-2])


# @lc code=end
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [10, 15, 20]
print(Solution().minCostClimbingStairs(cost))
