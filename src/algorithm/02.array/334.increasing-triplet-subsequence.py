#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
from typing import List


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


# @lc code=end
