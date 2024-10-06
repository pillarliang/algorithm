#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List

"""
组合问题：
Positive - Negative = target
Positive + Negative = Sum
==> Positive = (sum + target) / 2
==> 找出有多少种方案能从物品（nums) 中取出重量 Positive 来放入背包中。
确定子问题：用物品（nums）中前 i 个物品构成重量为 j 的重量的方法 table[i][j]。(注意是前 i 个物品，不是第 i 个。) 多维动态规划问题。
状态转移方程：对于每个数字 num，可以选择是否加入当前子集。如果不选，则子集和为 j 的数量为 dp[i-1][j]；如果选，则子集和为 j-num 的数量为 dp[i-1][j-num]。
"""


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        if (sum(nums) + target) % 2 != 0 or sum(nums) < abs(target):
            return 0

        # initial table
        target_sum = (sum(nums) + target) // 2
        table = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

        table[0][0] = 1

        for i in range(1, len(table)):
            for w in range(len(table[0])):
                table[i][w] = table[i - 1][w]
                if w >= nums[i - 1]:
                    table[i][w] += table[i - 1][w - nums[i - 1]]

        return table[len(nums)][target_sum]


# @lc code=end
