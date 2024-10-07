#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

"""
房屋围成了一个圈。因此，第一个房屋和最后一个房屋相邻，意味着它们不能同时被偷窃。
问题可以分解为两个线性房屋偷窃问题，从而求解出最大值。
- 不偷第一个房屋：求从第 2 个房屋到最后一个房屋之间的最大偷窃金额。
- 不偷最后一个房屋：求从第 1 个房屋到倒数第二个房屋之间的最大偷窃金额。
"""
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        table = [0] * len(nums)
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            table[i] = max(table[i - 2] + nums[i], table[i - 1])

        return table[-1]


# @lc code=end
