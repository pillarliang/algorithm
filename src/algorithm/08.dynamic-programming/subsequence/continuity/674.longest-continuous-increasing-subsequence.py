#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
from typing import List

"""
状态转移方程：

如果 nums[i] > nums[i-1]，则 dp[i] = dp[i-1] + 1，表示可以将当前元素 nums[i] 添加到之前的递增子序列中，递增子序列长度加 1。
如果 nums[i] <= nums[i-1]，则 dp[i] = 1，表示当前的元素与前一个元素不构成递增关系，因此重新开始新的子序列。
"""


# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        table = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                table[i] = table[i - 1] + 1

        return max(table)


# @lc code=end
