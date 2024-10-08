#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List

"""
可以多次买卖股票，问最大收益。
对于每一天 i，我们可以定义两个状态：
dp[i][0]：表示第 i 天结束时 没有持有股票 的最大利润。
dp[i][1]：表示第 i 天结束时 持有股票 的最大利润。

dp[i][0]=max(dp[i−1][0],dp[i−1][1]+prices[i]) # 不持有股票：1. 前一天不持有 2.前一天持有当天卖出。
dp[i][1]=max(dp[i−1][1],dp[i−1][0]−prices[i]) # 持有股票：1. 前一天持有，2 前一天不持有，当天买入。

"""


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = [[0, 0] for _ in range(len(prices))]
        table[0][1] = -prices[0]

        for i in range(1, len(prices)):
            table[i][0] = max(table[i - 1][0], table[i - 1][1] + prices[i])
            table[i][1] = max(table[i - 1][1], table[i - 1][0] - prices[i])  # 持有股票

        return table[-1][0]


# @lc code=end
