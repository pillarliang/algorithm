#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front_pos = 0
        back_pos = len(nums) - 1
        result = 0

        while front_pos <= back_pos:
            if nums[front_pos] == val:
                if nums[back_pos] == val:
                    back_pos -= 1
                else:
                    nums[front_pos], nums[back_pos] = nums[back_pos], nums[
                        front_pos]
                    front_pos += 1
                    back_pos -= 1
                    result += 1
            else:
                front_pos += 1
                result += 1

        return result


# @lc code=end
# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2

# nums = [3, 2, 2, 3]
# val = 3

nums = [3, 3, 3, 3]
val = 3
print(Solution().removeElement(nums, val))
