#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        front_pos = 0
        back_pos = 0
        result = float('inf')
        mid_value = nums[0]

        while front_pos <= back_pos and back_pos < len(nums):
            if nums[front_pos] == target:
                return 1
            if mid_value >= target:
                result = min(result, back_pos - front_pos + 1)
                mid_value -= nums[front_pos]
                front_pos += 1
            else:
                back_pos += 1
                if back_pos <= len(nums) - 1:
                    mid_value += nums[back_pos]

        return result if result != float('inf') else 0


# @lc code=end
# target = 7
# nums = [2, 3, 1, 2, 4, 3]

# target = 4
# nums = [1, 4, 4]

# target = 11
# nums = [1, 1, 1, 1, 1, 1, 1, 1]

target = 7
nums = [5]
print(Solution().minSubArrayLen(target, nums))
