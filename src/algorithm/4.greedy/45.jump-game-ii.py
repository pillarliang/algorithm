#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_distance = nums[0]
        next_distance = 0
        count = 1
        if len(nums) == 1:
            return 0

        for num_index in range(len(nums)):
            if cur_distance >= len(nums) - 1:
                return count
            next_distance = max(next_distance, num_index + nums[num_index])
            if num_index == cur_distance:
                cur_distance = next_distance
                count += 1


# @lc code=end

# nums = [2, 3, 1, 1, 4]
nums = [2, 3, 0, 1, 4]
# nums = [0]
# nums = [1, 2, 3]

print(Solution().jump(nums))
