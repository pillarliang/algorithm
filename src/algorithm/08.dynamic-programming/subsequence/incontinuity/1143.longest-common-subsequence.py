#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
"""
最长子序列，不一定连续。
"""


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        table = [
            [0] * (n + 1) for _ in range(m + 1)
        ]  # table[i][j] 表示 text1 的前 i 个字符和 text2 的前 j 个字符的最长公共子序列的长度。

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(
                        table[i - 1][j], table[i][j - 1]
                    )  # 比较上面和左面哪个值大
        return table[m][n]

    def longestCommonSubsequence_v2(self, text1: str, text2: str) -> int:
        table = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        return table[len(text2)][len(text1)]


# @lc code=end
