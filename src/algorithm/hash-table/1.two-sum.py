#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for index, item in enumerate(nums):
            if target - item in nums_dict:
                return [nums_dict[target - item], index]
            nums_dict[item] = index


# nums = [3, 3]
# target = 6

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))
