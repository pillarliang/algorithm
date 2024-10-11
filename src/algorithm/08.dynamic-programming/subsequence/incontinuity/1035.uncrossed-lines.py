#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#
from typing import List

"""
这个问题可以转化为最长公共子序列（Longest Common Subsequence, LCS）问题。
"""


# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        table = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]

        for i in range(1, len(nums2) + 1):
            for j in range(1, len(nums1) + 1):
                if nums2[i - 1] == nums1[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i][j - 1], table[i - 1][j])

        return table[len(nums2)][len(nums1)]


# @lc code=end
