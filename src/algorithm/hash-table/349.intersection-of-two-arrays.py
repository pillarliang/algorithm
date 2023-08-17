#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = defaultdict(int)
        nums2_dict = defaultdict(int)
        result_arr = []
        for i in nums1:
            nums1_dict[i] += 1

        for i in nums2:
            nums2_dict[i] += 1

        for i in nums2_dict.keys():
            if i in nums1_dict:
                result_arr.append(i)

        return result_arr


# @lc code=end
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersection(nums1, nums2))
