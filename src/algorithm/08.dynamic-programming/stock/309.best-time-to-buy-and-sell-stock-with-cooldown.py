#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
from typing import List

"""
我们需要定义三个状态来表示每天结束时的三种情况：

dp[i][0]：第 i 天结束时，不持有股票，且当天没有卖出股票（可能是冷冻期）。
dp[i][1]：第 i 天结束时，持有股票。
dp[i][2]：第 i 天结束时，不持有股票，且当天卖出了股票。
"""


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = [[0, 0, 0] for _ in range(len(prices))]

        table[0][1] = -prices[0]
        for i in range(1, len(prices)):
            table[i][0] = max(
                table[i - 1][0], table[i - 1][2]
            )  # 继承前一天的不持有状态; 继承前一天刚卖出的状态(冷冻期)
            table[i][1] = max(
                table[i - 1][1], table[i - 1][0] - prices[i]
            )  # 继承前一天持有股票的状态；从前一天不持有股票且不在冷冻期的状态转移过来买入股票
            table[i][2] = table[i - 1][1] + prices[i]  # 从前一天持有股票的状态卖出股票

        return max(table[-1][0], table[-1][2])


# @lc code=end
