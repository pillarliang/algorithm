#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_range = nums[0]
        if len(nums) == 1:
            return True

        for index, item in enumerate(nums):
            if index == len(nums) - 1 or max_range == 0:
                return False

            max_range = max(max_range - 1, item)
            if max_range >= len(nums) - 1 - index:
                return True

        return False


# @lc code=end

# nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
# nums = [0, 2, 3]
nums = [1, 0, 1, 0]

print(Solution().canJump(nums))
