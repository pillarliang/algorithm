#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List

"""
1. determine the subproblem:
The subproblem is to calculate the maximum value of the two choices at the i-th house.
- 
"""


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # 1. initialize the dp array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 2. state transition
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


# @lc code=end
