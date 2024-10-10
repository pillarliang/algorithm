#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List

"""
定义状态转移方程：
对于每个 i（当前元素），我们需要检查它之前的所有元素 j (0 <= j < i)，
如果 nums[i] > nums[j]，这意味着可以将 nums[i] 添加到以 nums[j] 结尾的递增子序列中。
因此我们可以更新 dp[i]：dp[i] = max(dp[i], dp[j] + 1)  # 当 nums[i] > nums[j] 时更新 dp[i]
"""

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    table[i] = max(table[i], table[j] + 1)
                    
        return max(table)
    
# @lc code=end

