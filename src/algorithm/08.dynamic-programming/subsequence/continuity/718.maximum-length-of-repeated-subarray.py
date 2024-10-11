#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
"""
子数组就是连续子序列。
"""
from typing import List


# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Find the maximum length of a subarray that appears in both nums1 and nums2.

        :param nums1: List of integers.
        :param nums2: List of integers.
        :return: The maximum length of the repeated subarray.
        """
        table = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        max_len = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                    max_len = max(max_len, table[i][j])

        return max_len


# @lc code=end
