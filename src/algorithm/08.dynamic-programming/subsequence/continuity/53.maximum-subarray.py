#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List

"""
注意：子问题 dp[i]，表示以第 i 个元素*结尾*的最大子数组和。
"""


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        table = [0] * len(nums)
        table[0] = nums[0]
        result = table[0]

        for i in range(1, len(nums)):
            table[i] = max(table[i - 1] + nums[i], nums[i])
            result = max(result, table[i])

        return result


# @lc code=end
