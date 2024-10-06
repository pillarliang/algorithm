#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
"""
最值问题：背包中最多能放多少个物品。
m 和 n 相当于是一个背包，两个维度的背包。物品中包含 0,1 的个数即 weight
循环是三层，table 是 2 维度, 每个物品只能使用一次 ==> 倒序遍历table
"""
from typing import List


# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 创建一个 (m+1) x (n+1) 的二维 dp 表
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeroes = s.count("0")
            ones = s.count("1")

            # 倒序遍历 dp 表，防止重复使用当前字符串
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    table[i][j] = max(table[i][j], table[i - zeroes][j - ones] + 1)

        return table[m][n]


# @lc code=end
