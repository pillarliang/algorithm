#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List

"""
股票只能买卖一次，问最大利润。
"""


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = [0] * len(prices)
        minmum = prices[0]

        for i in range(1, len(prices)):
            minmum = min(minmum, prices[i])
            table[i] = max(table[i - 1], prices[i] - minmum)

        return table[-1]


# @lc code=end
