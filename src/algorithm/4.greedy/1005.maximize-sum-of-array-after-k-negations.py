#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        while k > 0:
            k -= 1
            nums[0] = -nums[0]
            nums.sort()

        return sum(nums)


# @lc code=end

nums = [4, 2, 3]
k = 1

# nums = [3, -1, 0, 2]
# k = 3

# nums = [2, -3, -1, 5, -4]
# k = 2

# nums = [-2, 9, 9, 8, 4]
# k = 5
print(Solution().largestSumAfterKNegations(nums, k))
