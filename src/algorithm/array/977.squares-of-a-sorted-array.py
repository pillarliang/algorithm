#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        front_pos = 0
        back_pos = len(nums) - 1
        result_arr = []

        while front_pos <= back_pos:
            if pow(nums[front_pos], 2) <= nums[back_pos]**2:
                result_arr.insert(0, nums[back_pos]**2)
                back_pos -= 1
            else:
                result_arr.insert(0, pow(nums[front_pos], 2))
                front_pos += 1

        return result_arr


# @lc code=end
# nums = [-4, -1, 0, 3, 10]
nums = [-7, -3, 2, 3, 11]
print(Solution().sortedSquares(nums))
